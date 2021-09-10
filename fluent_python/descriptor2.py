import abc


class AutoStorge:
    __counter = 0  # 统计实例数量

    def __init__(self):
        cls = self.__class__  # cls 是 Quantity 类的引用
        prefix = cls.__name__  # NonBlank, Quantity
        index = cls.__counter
        self.storage_name = "_{}#{}".format(prefix, index)
        # 每个描述符的 名称是独一无二的，
        # 这种非法命名（#） ，内置的 getattr 和 setattr 可以接受
        cls.__counter += 1
        # storage_name 属性，
        # 这是托管实例中存储值的 属性的名称

    def __set__(self, instance, value):
        # self 是描述符 实例（即 LineItem.weight 或 LineItem.price）
        # instance 是 托管实例（LineItem 实例）
        setattr(instance, self.storage_name, value) # 没有验证，交给Validated

    def __get__(self, instance, owner):
        if instance is None:
            return self
        return getattr(instance, self.storage_name)


class Validated(abc.ABC, AutoStorge):
    def __set__(self, instance, value):
        value = self.validate(instance, value)
        #  __set__ 方法把验证操作委托给 validate 方法
        super().__set__(instance, value)
        # 然后把返回的 value 传给超类的 __set__ 方法，存储值

    @abc.abstractmethod # 在这个类中，validate 是抽象方法
    def validate(self, instance, value):
        """to do"""


class Quantity(Validated): # 继承自 Validated 类
    def validate(self, instance, value): # 检查非正数
        if value <= 0:
            raise ValueError("value should be positive")
        return value

class NonBlank(Validated): # 继承自 Validated 类
    """a string with at least one non-space character"""
    def validate(self, instance, value):
        value = value.strip() # 去除首尾空白
        if len(value) == 0:
            raise ValueError('value cannot be empty or blank')
        return value

class LineItem:
    description = NonBlank() # '_NonBlank#0'
    weight = Quantity()  # '_Quantity#0'
    # 描述符实例绑定给 weight 属性， 类属性，所有 LineItem实例共享
    price = Quantity()  # '_Quantity#1'

    def __init__(self, description, weight, price):
        self.description = description
        self.weight = weight
        self.price = price

    def subtotal(self):
        return self.weight * self.price


coconuts = LineItem('  Brazilian coconut  ', 20, 17.95)
print(coconuts.weight, coconuts.price) # 20 17.95
print(getattr(coconuts, '_NonBlank#0')) #Brazilian coconut
print(getattr(coconuts, '_Quantity#0'), getattr(coconuts, '_Quantity#1'))
# 20 17.95
print(LineItem.weight) # <__main__.Quantity object at 0x0000012B2A9AF9A0>

