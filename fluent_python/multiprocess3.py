import time
import sys
import os
import asyncio
import aiohttp

POP20_CC = ('CN IN US ID BR PK NG BD RU JP ' 'MX PH VN ET EG DE IR TR CD FR').split()
BASE_URL = 'http://flupy.org/data/flags'
DEST_DIR = './'


def save_flag(img, filename):  # 保存图像
    path = os.path.join(DEST_DIR, filename)
    with open(path, 'wb') as fp:
        fp.write(img)


def show(text):  # 打印信息
    print(text, end=' ')
    sys.stdout.flush()


async def get_flag(cc):  # 获取图像
    url = '{}/{cc}/{cc}.gif'.format(BASE_URL, cc=cc.lower())
    async with aiohttp.request("GET", url) as resp:
        image = await resp.read()
    return image


async def download_one(cc):
    image = await get_flag(cc)
    show(cc)
    save_flag(image, cc.lower() + '.gif')
    return cc


def download_many_(cc_list):
    loop = asyncio.get_event_loop()
    todo = [download_one(cc) for cc in sorted(cc_list)] # 协程对象
    wait_coro = asyncio.wait(todo) # 包装成 task，wait是协程函数，返回协程或者生成器对象
    res, _ = loop.run_until_complete(wait_coro)
    # 驱动协程，返回 第一个元素是一系列结束的期物，第二个元素是一系列未结束的期物
    # loop.close()，好像不需要这句 上面 with 处可能自动关闭了
    return len(res)


def main(download_many):
    t0 = time.time()
    count = download_many(POP20_CC)
    elapsed = time.time() - t0
    msg = '\n{} flags downloaded in {:.2f}s'
    print(msg.format(count, elapsed))  # 计时信息


if __name__ == '__main__':
    main(download_many_)
