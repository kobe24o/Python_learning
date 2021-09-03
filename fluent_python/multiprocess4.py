import collections
import time
import sys
import os
import asyncio
from http import HTTPStatus

import aiohttp
from aiohttp import web
import tqdm

POP20_CC = ('CN IN US ID BR PK NG BD RU JP ' 'MX PH VN ET EG DE IR TR CD FR').split()
BASE_URL = 'http://flupy.org/data/flags'
DEST_DIR = './'
DEFAULT_CONCUR_REQ = 5
MAX_CONCUR_REQ = 1000


class FetchError(Exception):
    def __init__(self, country_code):
        self.country_code = country_code


def save_flag(img, filename):  # 保存图像
    path = os.path.join(DEST_DIR, filename)
    with open(path, 'wb') as fp:
        fp.write(img*1000)


def show(text):  # 打印信息
    print(text, end=' ')
    sys.stdout.flush()


async def get_flag(cc):  # 获取图像
    url = '{}/{cc}/{cc}.gif'.format(BASE_URL, cc=cc.lower())
    async with aiohttp.request("GET", url) as resp:
        if resp.status == 200:
            image = await resp.read()
            return image
        elif resp.status == 404:
            raise web.HTTPNotFound()
        else:
            raise aiohttp.WebSocketError(code=resp.status, message=resp.reason)


async def download_one(cc, semaphore, verbose):
    try:
        async with semaphore:
            image = await get_flag(cc)
    except web.HTTPNotFound:
        status = HTTPStatus.NOT_FOUND
        msg = "not found"
    except Exception as exc:
        raise FetchError(cc) from exc
    else:
        # 因此保存文件时，整个应用程序都会冻结,为了避免，使用下面方法
        loop = asyncio.get_event_loop()  # 获取事件循环对象的引用
        loop.run_in_executor(None,  # 方法的第一个参数是 Executor 实例；
                             # 如果设为 None，使用事件循环的默认 ThreadPoolExecutor 实例
                             save_flag, image, cc.lower() + ".gif")
                            #  余下的参数是可调用的对象，以及可调用对象的位置参数
        status = HTTPStatus.OK
        msg = "OK"
    if verbose and msg:
        print(cc, msg)
    return (status, cc)


async def downloader_coro(cc_list, verbose, concur_req):  # 协程函数
    counter = collections.Counter()
    semaphore = asyncio.Semaphore(value=concur_req)  # 最多可以使用这个计数器的协程个数
    todo = [download_one(cc, semaphore, verbose=True) for cc in sorted(cc_list)]  # 协程对象列表
    todo_iter = asyncio.as_completed(todo)  # 获取迭代器，会在期物运行结束后返回期物
    if not verbose:
        todo_iter = tqdm.tqdm(todo_iter, total=len(cc_list))  # 迭代器传给tqdm，显示进度条
    for future in todo_iter:  # 迭代器运行结束的期物
        try:
            res = await future  # 获取期物对象的结果
        except FetchError as exc:
            country_code = exc.country_code
            try:
                error_msg = exc.__cause__.args[0]
            except IndexError:
                error_msg = exc.__cause__.__class__.__name__
            if verbose and error_msg:
                msg = '*** Error for {}: {}'
                print(msg.format(country_code, error_msg))
            status = HTTPStatus.error
        else:
            status = res[0]
        counter[status] += 1  # 记录结果
    return counter  # 返回计数器


def download_many_(cc_list, verbose, concur_req):
    loop = asyncio.get_event_loop()
    coro = downloader_coro(cc_list, verbose=verbose, concur_req=concur_req)
    # 实例化 downloader_coro协程，然后通过 run_until_complete 方法把它传给事件循环
    counts = loop.run_until_complete(coro)
    # loop.close() # 好像不需要这句 上面 with 处可能自动关闭了
    return counts


def main(download_many):
    t0 = time.time()
    count = download_many(POP20_CC, True, MAX_CONCUR_REQ)
    elapsed = time.time() - t0
    msg = '\n{} flags downloaded in {:.2f}s'
    print(msg.format(count, elapsed))  # 计时信息


if __name__ == '__main__':
    main(download_many_)
