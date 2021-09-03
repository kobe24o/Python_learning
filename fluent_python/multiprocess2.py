import asyncio
import itertools
import sys


# https://docs.python.org/3.8/library/asyncio.html
async def spin(msg): # py3.5以后的新语法 async / await，协程函数
    write, flush = sys.stdout.write, sys.stdout.flush
    for char in itertools.cycle("|/-\\"):  # 无限循环
        status = char + ' ' + msg
        write(status)
        flush()
        write("\x08" * len(status))  # \x08 退格键，光标移动回去
        try:
            await asyncio.sleep(0.1)
        except asyncio.CancelledError: # 遇到取消异常，退出循环
            print("cancel")
            break
    write(' ' * len(status) + "\x08" * len(status))
    print("end spin")


async def slow_function(): # 协程函数
    print("start IO")
    await asyncio.sleep(3) # 假装进行 IO 操作
    print("end IO  ")
    return 42


async def supervisor():  # 协程函数
    spinner = asyncio.ensure_future(spin("thinking!")) # spinner 排定任务
    print("spinner object:", spinner)  # 显示从属线程对象
    # spinner object: <Task pending coro=<spin() running at D:\ >
    print("start slow")
    result = await slow_function()
    print("end slow")
    spinner.cancel() # task对象可以取消，抛出CancelledError异常
    return result


def main():
    loop = asyncio.get_event_loop() # 获取事件循环的引用
    result = loop.run_until_complete(supervisor())  # 驱动 supervisor 协程，让它运行完毕
    loop.close()
    print("answer:", result)


if __name__ == '__main__':
    main()
