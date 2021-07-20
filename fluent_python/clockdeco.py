# 装饰器示例
# clockdeco.py  输出函数运行时间
import time
def clock(func):
    def clocked(*args): # 内部函数 clocked
        t0 = time.perf_counter()
        res = func(*args) # clocked的闭包中包含自由变量 func
        elapsed = time.perf_counter() - t0
        name = func.__name__
        arg_str = ','.join(repr(arg) for arg in args)
        print('[%0.8fs] %s(%s) -> %r' % (elapsed, name, arg_str, res))
        # 打印 时间， 函数名， 参数名， 函数结果
        return res
    return clocked # 返回内部函数，取代被装饰的函数
