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

    import time
    from clockdeco import clock


    @clock
    def testFunc(seconds):
        time.sleep(seconds)


    @clock
    def fact(n):
        return 1 if n < 2 else n * fact(n - 1)


    testFunc(.123)
    fact(6)
