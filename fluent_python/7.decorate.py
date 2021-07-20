import functools
import numbers


def deco(func):
    def inner():
        print("running inner()")

    return inner  # deco 返回 inner 函数对象


@deco
def target():
    print('running target()')


target()  # running inner() 调用被装饰的 target，运行的是 inner
print(target)  # <function deco.<locals>.inner at 0x000001B66CBBD3A0>
# target 是 inner 的引用

registry = []


def register(func):
    print('running register(%s)' % func)
    registry.append(func)
    return func


@register
def f1():
    print('running f1()')


@register
def f2():
    print('running f2()')


def f3():
    print('running f3()')


def main():
    print('running main()')
    print('registry ->', registry)
    f1()
    f2()
    f3()


if __name__ == '__main__':
    main()
    # running register(<function f1 at 0x000002770981D550>) # 装饰器导入时立即运行
    # running register(<function f2 at 0x000002770981D430>) # 装饰器导入时立即运行
    # running main()
    # registry -> [<function f1 at 0x000002770981D550>, <function f2 at 0x000002770981D430>]
    # running f1()
    # running f2()
    # running f3()

    # import time
    # from clockdeco import clock
    #
    #
    # @clock
    # def testFunc(seconds):
    #     time.sleep(seconds)
    #
    #
    # @clock
    # def fact(n):
    #     return 1 if n < 2 else n * fact(n - 1)
    #
    #
    # testFunc(.123)
    # fact(6)
    # print(fact.__name__)  # clocked

    from clockdeco2 import clock


    @clock
    def fact(n):
        return 1 if n < 2 else n * fact(n - 1)


    fact(6)
    print(fact.__name__)  # fact


    @functools.lru_cache
    @clock
    def fibonacci(n):
        if n < 2:
            return n
        return fibonacci(n - 2) + fibonacci(n - 1)


    print(fibonacci(6))

    # -----------------------------
    import numbers


    @functools.singledispatch
    def testFunc(val):
        return "{}".format(val)


    @testFunc.register(str)
    def _(val):
        return val + " add str"


    @testFunc.register(numbers.Integral)
    def _(val):
        return str(val + 100)


    @testFunc.register(tuple)
    def _(val):
        return ",".join(testFunc(v) for v in val)


    print(testFunc(5))
    print(testFunc("hello"))
    print(testFunc((5, "hello", (6, 7))))

    # --------------------------------------
    print("running start ")
    registry = set()

    def register(active=True): # 装饰器工厂函数, 必须加() 调用，传入参数，返回装饰器
        def decorate(func):
            print('running register(active=%s)->decorate(%s)' % (active, func))
            if active:
                registry.add(func)
            else:
                registry.discard(func)
            return func # 装饰器必须返回函数

        return decorate


    @register(active=False)
    def f1():
        print('running f1()')

    @register()
    def f2():
        print('running f2()')

    def f3():
        print('running f3()')

    print(registry)
    f1()
    f2()
    f3()

# ----------------------------
    import time

    DEFAULT_FMT = '[{elapsed:0.8f}s] {name}({args}) -> {result}'


    def clock(fmt=DEFAULT_FMT): # 参数化装饰器工厂函数
        def decorate(func): # 真正的装饰器
            def clocked(*_args): # 包装被装饰的函数
                t0 = time.time()
                _result = func(*_args) # 被装饰函数返回的真正结果
                elapsed = time.time() - t0
                name = func.__name__
                args = ', '.join(repr(arg) for arg in _args)
                result = repr(_result)
                print(fmt.format(**locals())) # **locals() 在 fmt 中引用 clocked 的局部变量
                return _result # clocked 会取代被装饰的函数，它应该返回被装饰的函数返回的值
            return clocked # decorate 返回 clocked
        return decorate # clock 返回 decorate


    @clock() # 不传参数，使用默认的
    def snooze(seconds):
        time.sleep(seconds)
    for i in range(3):
        snooze(.123)
    # [0.13069201s] snooze(0.123) -> None
    # [0.13592529s] snooze(0.123) -> None
    # [0.13488460s] snooze(0.123) -> None

    @clock('{name}: {elapsed}s')
    def snooze(seconds):
        time.sleep(seconds)
    for i in range(3):
        snooze(.123)
    # snooze: 0.134782075881958s
    # snooze: 0.1345205307006836s
    # snooze: 0.13508963584899902s

    @clock('{name}({args}) dt={elapsed:0.3f}s')
    def snooze(seconds):
        time.sleep(seconds)
    for i in range(3):
        snooze(.123)
    # snooze(0.123) dt = 0.134s
    # snooze(0.123) dt = 0.135s
    # snooze(0.123) dt = 0.135s
