import inspect


def simple_coroutine():  # 协程使用生成器函数定义，有yield关键字
    print("-> coroutine started")
    x = yield  # yield 右边没有表达式，所以只需从客户那里接收数据
    print("-> coroutine received: ", x)


my_coro = simple_coroutine()  # 调用函数，得到生成器对象
print(my_coro)
# <generator object simple_coroutine at 0x00000192FD458E40>
print(inspect.getgeneratorstate((my_coro)))  # GEN_CREATED 等待开始
print(next(my_coro))  # 调用next 到 yield 处暂停
# -> coroutine started
# None
print(inspect.getgeneratorstate((my_coro)))  # GEN_SUSPENDED 在 yield 出暂停
try:
    my_coro.send(24)  # 调用send，yield 会计算出24，之后协程恢复，
# 一直运行到下一个 yield 表达式，或者到达终止迭代
# -> coroutine received:  24
# Traceback (most recent call last):
# File "D:/gitcode/Python_learning/fluent_python/coroutine.py", line 12, in <module>
# my_coro.send(24)
# StopIteration
except:
    pass
print(inspect.getgeneratorstate((my_coro)))  # GEN_CLOSED 执行结束


def simple_coroutine2(a):
    print("-> started: a = ", a)
    b = yield a  # = 号右边的代码先执行，并暂停
    print("-> Received: b = ", b)
    c = yield a + b
    print("-> Received: c = ", c)


my_coro2 = simple_coroutine2(24)
print(inspect.getgeneratorstate((my_coro2)))  # GEN_CREATED
print(next(my_coro2))  # -> started: a =  24
# 24
print(inspect.getgeneratorstate((my_coro2)))  # GEN_SUSPENDED
print(my_coro2.send(6))  # -> Received: b =  6
# 30
try:
    print(my_coro2.send(3))  # -> Received: c =  3
except:
    pass
print(inspect.getgeneratorstate((my_coro2)))  # GEN_CLOSED


def avg():
    tot = 0.0
    count = 0
    average = None
    while True:
        term = yield average
        tot += term
        count += 1
        average = tot / count


a = avg()
a.send(None)
print(a.send(2))  # 2.0
print(a.send(3))  # 2.5
print(a.close())  # None
# print(a.send(3))  # StopIteration


from functools import wraps


def coroutine(func):
    @wraps(func)
    def primer(*args, **kwargs):  # 被装饰的生成器函数替换成 primer函数
        gen = func(*args, **kwargs)  # 调用被装饰的函数，获取生成器对象
        next(gen)  # 预激生成器
        return gen  # 返回生成器

    return primer


class DemoException(Exception):
    pass

def demo_exc_handling():
    print("-> coroutine started")
    while True:
        try:
            x = yield
        except DemoException:
            print("*** DemoException handled. continuing")
        else:
            print("-> coroutine received: {!r}".format(x))
    raise RuntimeError("This line should never run.")
    # 上面处理了异常，这一行永远不会被执行

exc_coro = demo_exc_handling()
next(exc_coro) # -> coroutine started
exc_coro.send(11) # -> coroutine received: 11
exc_coro.send(12) # -> coroutine received: 12
exc_coro.close()
print(inspect.getgeneratorstate(exc_coro)) # GEN_CLOSED

exc_coro = demo_exc_handling()
next(exc_coro) # -> coroutine started
exc_coro.send(11) # -> coroutine received: 11
exc_coro.throw(DemoException) # *** DemoException handled. continuing
print(inspect.getgeneratorstate(exc_coro)) # GEN_SUSPENDED

exc_coro = demo_exc_handling()
next(exc_coro) # -> coroutine started
exc_coro.send(11) # -> coroutine received: 11
# exc_coro.throw(ZeroDivisionError)
# Traceback (most recent call last):
# File "D:/gitcode/Python_learning/fluent_python/coroutine.py", line 116, in <module>
# exc_coro.throw(ZeroDivisionError)
# File "D:/gitcode/Python_learning/fluent_python/coroutine.py", line 92, in demo_exc_handling
# x = yield
# ZeroDivisionError

print("--------------")
def demo_finally():
    print("-> coroutine started")
    try:
        while True:
            try:
                x = yield
            except DemoException:
                print("*** DemoException handled. continuing")
            else:
                print("-> coroutine received: {!r}".format(x))
    finally:
        print("-> coroutine ending")

exc_coro = demo_finally()
next(exc_coro)
exc_coro.send(10)
exc_coro.throw(DemoException)
exc_coro.send(12)
# -> coroutine started
# -> coroutine received: 10
# *** DemoException handled. continuing
# -> coroutine received: 12
# -> coroutine ending


from collections import namedtuple
res = namedtuple("Result", "count average")

def averager():
    tot = 0.0
    count = 0
    avg = None
    while True:
        term = yield
        if term is None:
            break # 为了返回值，协程必须正常终止
        tot += term
        count += 1
        avg = tot/count
    return res(count, avg)
coro_avg = averager()
next(coro_avg)
coro_avg.send(10)
coro_avg.send(20)
coro_avg.send(30)
# coro_avg.send(None) # 发送None终止循环，协程结束
# Traceback (most recent call last):
# File "D:/gitcode/Python_learning/fluent_python/coroutine.py", line 170, in <module>
# coro_avg.send(None)
# StopIteration: Result(count=3, average=20.0)

print("*************")
coro_avg = averager()
next(coro_avg)
coro_avg.send(10)
coro_avg.send(20)
coro_avg.send(30)
try:
    coro_avg.send(None)
except StopIteration as exc:
    result = exc.value
print(result)
# Result(count=3, average=20.0)

def gen():
    yield from "AB"
    yield from range(1,3)
print(list(gen())) # ['A', 'B', 1, 2]