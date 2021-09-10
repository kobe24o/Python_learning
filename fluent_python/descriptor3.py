### 辅助函数，仅用于显示 ###
#
def cls_name(obj_or_cls):
    cls = type(obj_or_cls)
    if cls is type:
        cls = obj_or_cls
    return cls.__name__.split('.')[-1]


def display(obj):
    cls = type(obj)
    if cls is type:
        return '<class {}>'.format(obj.__name__)
    elif cls in [type(None), int]:
        return repr(obj)
    else:
        return '<{} object>'.format(cls_name(obj))


def print_args(name, *args):
    pseudo_args = ', '.join(display(x) for x in args)
    print('-> {}.__{}__({})'.format(cls_name(args[0]), name, pseudo_args))


class Overriding:
    """也称数据描述符或强制描述符"""

    def __get__(self, instance, owner):
        print_args('get', self, instance, owner)

    def __set__(self, instance, value):
        print_args('set', self, instance, value)


class OverridingNoGet:
    """没有``__get__``方法的覆盖型描述符"""

    def __set__(self, instance, value):
        print_args('set', self, instance, value)


class NonOverriding:
    """也称非数据描述符 或 非遮盖型描述符"""

    def __get__(self, instance, owner):
        print_args('get', self, instance, owner)


class Managed:
    over = Overriding()
    over_no_get = OverridingNoGet()
    non_over = NonOverriding()

    def spam(self):
        print('-> Managed.spam({})'.format(display(self)))


obj = Managed()
obj.over  # obj.over 触发描述符的 __get__ 方法, 第二个参数的值是托管实例 obj
# -> Overriding.__get__(<Overriding object>, <Managed object>, <class Managed>)
Managed.over  # Managed.over 触发描述符的 __get__ 方法，第二个参数 （instance）的值是 None
# -> Overriding.__get__(<Overriding object>, None, <class Managed>)
obj.over = 7  # 为 obj.over 赋值，触发描述符的 __set__ 方法，最后一个参数的 值是 7
# -> Overriding.__set__(<Overriding object>, <Managed object>, 7)
obj.over  # 会触发描述符的 __get__ 方法
# -> Overriding.__get__(<Overriding object>, <Managed object>, <class Managed>)
obj.__dict__['over'] = 8  # 跳过描述符，直接通过 obj.__dict__ 属性设值
print(vars(obj))  # {'over': 8} #  确认值在 obj.__dict__ 属性中，在 over 键名下
obj.over  # 然而，即使是名为 over 的实例属性，Managed.over 描述符仍会覆盖读取 obj.over 这个操作
# -> Overriding.__get__(<Overriding object>, <Managed object>, <class Managed>)
print("-------------")

# 这个覆盖型描述符没有 __get__ 方法，因此，obj.over_no_get 从 类 中获取描述符实例
print(obj.over_no_get)      # <__main__.OverridingNoGet object at 0x000001BC57E3FA90>
# 直接从托管类中读取描述符实例也是如此
print(Managed.over_no_get)  # <__main__.OverridingNoGet object at 0x000001BC57E3FA90>
# obj.over_no_get 赋值会触发描述符的 __set__ 方法
obj.over_no_get = 7
# -> OverridingNoGet.__set__(<OverridingNoGet object>, <Managed object>, 7)
print(obj.over_no_get)      # <__main__.OverridingNoGet object at 0x000001BC57E3FA90>
#  通过实例的 __dict__ 属性设置名为 over_no_get 的实例属性
obj.__dict__['over_no_get'] = 9
# 现在，over_no_get 实例属性会遮盖描述符，但是只有 读 操作是如此
print(obj.over_no_get)  # 9
# 为 obj.over_no_get 赋值，仍然经过描述符的 __set__ 方法处理
obj.over_no_get = 7
# -> OverridingNoGet.__set__(<OverridingNoGet object>, <Managed object>, 7)
# 但是读取时，只要有同名的实例属性，描述符就会被遮盖
print(obj.over_no_get)  # 9


print('-------------')

# obj.non_over 触发描述符的 __get__ 方法，第二个参数的值是 obj
obj.non_over
# -> NonOverriding.__get__(<NonOverriding object>, <Managed object>, <class Managed>)
# Managed.non_over 是非覆盖型描述符，因此没有干涉赋值操作的 __set__ 方法
obj.non_over = 7
print(obj.non_over) # 7 现在，obj 有个名为 non_over 的实例属性，把 Managed 类的同名 描述符属性遮盖掉
Managed.non_over # Managed.non_over 描述符依然存在，会通过 类 截获这次访问
# -> NonOverriding.__get__(<NonOverriding object>, None, <class Managed>)
del obj.non_over # 如果把 non_over 实例 属性删除了
obj.non_over # 读取 obj.non_over 时，会触发类中描述符的 __get__ 方法；但要注意，第二个参数的值是托管实例
# -> NonOverriding.__get__(<NonOverriding object>, <Managed object>, <class Managed>)

obj = Managed()
Managed.over = 1
Managed.over_no_get = 2
Managed.non_over = 3
print(obj.over, obj.over_no_get, obj.non_over) # 1 2 3

print(obj.spam)
# <bound method Managed.spam of <__main__.Managed object at 0x000001E86E4CEAF0>>
print(Managed.spam)
# <function Managed.spam at 0x000001584C5B63A0>
obj.spam = 7
print(obj.spam) # 7
