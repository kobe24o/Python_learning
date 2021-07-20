# 装饰器示例
# clockdeco2.py  输出函数运行时间
import time
import functools


def clock(func):
    @functools.wraps(func)
    def clocked(*args, **kwargs):  # 内部函数 clocked
        t0 = time.perf_counter()
        res = func(*args, **kwargs)  # clocked的闭包中包含自由变量 func
        elapsed = time.perf_counter() - t0
        name = func.__name__
        arg_lst = []
        if args:
            arg_lst.append(', '.join(repr(arg) for arg in args))
        if kwargs:
            pairs = ['%s=%r' % (k, w) for k, w in sorted(kwargs.items())]
            arg_lst.append(', '.join(pairs))
        arg_str = ', '.join(arg_lst)
        print('[%0.8fs] %s(%s) -> %r' % (elapsed, name, arg_str, res))
        # 打印 时间， 函数名， 参数名， 函数结果
        return res

    return clocked  # 返回内部函数，取代被装饰的函数
