import os
import time
import sys
import requests

POP20_CC = ('CN IN US ID BR PK NG BD RU JP ' 'MX PH VN ET EG DE IR TR CD FR').split()
BASE_URL = 'http://flupy.org/data/flags'
DEST_DIR = './'


def save_flag(img, filename):  # 保存图像
    path = os.path.join(DEST_DIR, filename)
    with open(path, 'wb') as fp:
        fp.write(img)


def get_flag(cc):  # 获取图像
    url = '{}/{cc}/{cc}.gif'.format(BASE_URL, cc=cc.lower())
    resp = requests.get(url)
    return resp.content


def show(text):  # 打印信息
    print(text, end=' ')
    sys.stdout.flush()


def download_many(cc_list):
    for cc in sorted(cc_list):
        image = get_flag(cc)  # 获取
        show(cc)  # 打印
        save_flag(image, cc.lower() + '.gif')  # 保存
    return len(cc_list)


def main(download_many):
    t0 = time.time()
    count = download_many(POP20_CC)
    elapsed = time.time() - t0
    msg = '\n{} flags downloaded in {:.2f}s'
    print(msg.format(count, elapsed))  # 计时信息


# ----使用 futures.ThreadPoolExecutor 类实现多线程下载
from concurrent import futures

MAX_WORKERS = 20  # 最多使用几个线程


def download_one(cc):
    image = get_flag(cc)
    show(cc)
    save_flag(image, cc.lower() + '.gif')
    return cc


def download_many_1(cc_list):
    workers = min(MAX_WORKERS, len(cc_list))
    with futures.ThreadPoolExecutor(workers) as executor:
        #  使用工作的线程数实例化 ThreadPoolExecutor 类；
        #  executor.__exit__ 方法会调用 executor.shutdown(wait=True) 方法，
        #  它会在所有线程都执行完毕 前阻塞线程
        res = executor.map(download_one, sorted(cc_list))
        # download_one 函数 会在多个线程中并发调用；
        # map 方法返回一个生成器，因此可以迭代， 获取各个函数返回的值
    return len(list(res))

def download_many_2(cc_list):
    cc_list = cc_list[:5]
    with futures.ThreadPoolExecutor(max_workers=3) as executor:
        to_do = []
        for cc in sorted(cc_list):
            future = executor.submit(download_one, cc)
            # executor.submit 方法排定可调用对象的执行时间，
            # 然后返回一个 期物，表示这个待执行的操作
            to_do.append(future) # 存储各个期物
            msg = 'Scheduled for {}: {}'
            print(msg.format(cc, future))
        results = []
        for future in futures.as_completed(to_do):
            # as_completed 函数在期物运行结束后产出期物
            res = future.result() # 获取期物的结果
            msg = '{} result: {!r}'
            print(msg.format(future, res))
            results.append(res)
    return len(results)
if __name__ == '__main__':
    # main(download_many) # 24 秒
    # main(download_many_1)  # 3 秒
    main(download_many_2)