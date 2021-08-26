for i in range(3):
    print(i)
else:
    print("finish, no break")
    # finish, no break

for i in range(3):
    if i == 2:
        break
    print(i)
else:
    print("break")
    # 无输出

i = 0
while i < 3:
    print(i)
    i += 1
else:
    print("no break")  # no break
i = 0
while i < 3:
    if i == 2:
        break
    print(i)
    i += 1
else:
    print("break")  # 无输出

arr = [0]
try:
    arr[0] = 1
except:
    print("error")  # 无输出
else:
    print("no error, run else")
    # no error, run else

arr = []
try:
    arr[0] = 0
except:
    print("error")  # error
else:
    print("error, will not run else")  # 无输出
finally:
    print("finish")  # finish


class LookingGlass:
    def __enter__(self):  # 没有其它的参数了
        import sys
        self.original_write = sys.stdout.write
        sys.stdout.write = self.reverse_write
        return 'ABCD'

    def reverse_write(self, text):  # 反转字符串，实现输出
        self.original_write(text[::-1])

    def __exit__(self, exc_type, exc_value, traceback):
        # exc_type 异常类
        # exc_value 异常实例
        # traceback 对象
        # 在 try/finally 语句的 finally 块中调用 sys.exc_info()
        # 得到的就是 __exit__ 接收的这三个参数
        import sys
        sys.stdout.write = self.original_write
        if exc_type is ZeroDivisionError:
            print('Please DO NOT divide by zero!')
            return True


with LookingGlass() as what:
    # 进入 __enter__ 函数时返回的 ABCD 字符串存入 what
    print("Michael learning python")
    # nohtyp gninrael leahciM
    print(what)
    # DCBA
print("Michael learning python")
# Michael learning python
print(what)
# ABCD

manager = LookingGlass()
print(manager)
# <__main__.LookingGlass object at 0x00000231226F2190>
string = manager.__enter__()
print(string)  # DCBA
print(string == "ABCD")  # eurT, 所有的输出经过管理器的 反向输出处理了
print(string == "DCBA")  # eslaF, 所有的输出经过管理器的 反向输出处理了
print(manager)
# >0912F62213200000x0 ta tcejbo ssalGgnikooL.__niam__<
manager.__exit__(None, None, None)  # 还原了正常的输出
print(string)  # ABCD

import contextlib


@contextlib.contextmanager
def looking_glass1():
    import sys
    original_write = sys.stdout.write

    def reverse_write(text):
        original_write(text[::-1])

    sys.stdout.write = reverse_write
    yield 'ABCD'  # 产出的值绑定到 as 目标上
    # 执行 with 块代码时，函数会在这里暂停
    sys.stdout.write = original_write
    #  控制权一旦跳出 with 块，继续执行 yield 语句之后的代码


with looking_glass1() as what:
    print("Michael learning python")
    print(what)
# nohtyp gninrael leahciM
# DCBA
print("Michael learning python")
print(what)
# Michael learning python
# ABCD
