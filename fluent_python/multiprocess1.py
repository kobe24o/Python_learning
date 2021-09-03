import threading
import itertools
import time
import sys


class Signal:
    go = True


def spin(msg, signal):
    write, flush = sys.stdout.write, sys.stdout.flush
    for char in itertools.cycle("|/-\\"):  # 无限循环
        status = char + ' ' + msg
        write(status)
        flush()
        write("\x08" * len(status))  # \x08 退格键，光标移动回去
        time.sleep(0.1)
        if not signal.go:
            break
    write(' ' * len(status) + "\x08" * len(status))
    # 使用空格清除状态消息，把光标移回开头


def slow_function():  # 假设是一个耗时的计算过程
    time.sleep(10)  # sleep 会阻塞主线程，释放GIL，创建从属线程
    return 42


def supervisor():  # 该函数，设置从属线程，显示线程对象，运行耗时的计算，最后杀死线程
    signal = Signal()
    spinner = threading.Thread(target=spin, args=("thinking!", signal))
    print("spinner object:", spinner)  # 显示从属线程对象
    spinner.start()  # 启动从属线程
    result = slow_function()  # 运行计算程序，阻塞主线程，从属线程动画显示旋转指针
    signal.go = False  # 改变signal 状态，终止 spin 中的for循环
    spinner.join()  # 等待spinner线程结束
    return result


def main():
    result = supervisor()  # 运行 supervisor
    print("Answer:", result)


if __name__ == '__main__':
    main()
