import keyword
from urllib.request import urlopen
import warnings
import os
import json

URL = 'http://www.oreilly.com/pub/sc/osconfeed'
JSON = './osconfeed.json'

from collections import abc


class FrozenJSON:
    # 一个只读接口，使用属性表示法访问JSON类对象
    def __new__(cls, arg):  # 第一个参数是类本身
        if isinstance(arg, abc.Mapping):
            return super().__new__(cls)
        elif isinstance(arg, abc.MutableSequence):
            return [cls(item) for item in arg]
        else:
            return arg

    def __init__(self, mapping):
        self.__data = {}
        for k, v in mapping.items():
            if keyword.iskeyword(k):
                k += "_"
            if not k.isidentifier():
                k = "_" + k
            self.__data[k] = v

    def __getattr__(self, name):
        if hasattr(self.__data, name):  # 有属性，获取
            return getattr(self.__data, name)
            # 调用 keys 等方法就是通过这种方式处理的
        else:  # 没有，构建 FrozenJSON
            return FrozenJSON(self.__data[name])


grad = FrozenJSON({'name': 'Jim Bo', 'class': 1982})
# print(grad.class) # invalid syntax
# print(getattr(grad, 'class')) # 1982
print(grad.class_)

grad = FrozenJSON({'2name': 'Jim Bo', 'class': 1982})
print(grad._2name)  # SyntaxError: invalid syntax


class Class:
    data = "class data attr"

    @property
    def prop(self):
        return "prop value"


obj = Class()
print(vars(obj))  # {}, vars 函数返回 obj 的 __dict__ 属性
print(obj.data)  # class data attr
obj.data = "changed"
print(vars(obj))  # {'data': 'changed'}
print(Class.data)  # class data attr
# 实例修改了data，但是 类属性没有被修改

print(Class.prop)  # <property object at 0x0000021A91E4A680>
print(obj.prop)  # prop value
# obj.prop = "changed prop"  # 报错 can't set attribute
obj.__dict__["prop"] = "changed prop1"
print(vars(obj))  # {'data': 'changed', 'prop': 'changed prop1'}
print(obj.prop)  # prop value #
# 读取 obj.prop 时仍会运行特性的读值方法。特性没被实例属性遮盖
Class.prop = "haha"  # 覆盖 Class.prop 特性，销毁特性对象
print(obj.prop)  # changed prop1
# 现在，obj.prop 获取的是实例属性。
# Class.prop 不是特性了，因此不会再覆盖 obj.prop。

print(obj.data)  # changed
print(Class.data)  # class data attr
Class.data = property(lambda self: "data prop value")
# 使用新特性覆盖 Class.data
print(obj.data)  # data prop value
# obj.data 被 Class.data 特性遮盖了
del Class.data  # 删除特性
print(obj.data)  # changed


# 恢复原样，obj.data 获取的是实例属性 data


def quantity(storage_name):
    def qty_getter(instance):
        return instance.__dict__[storage_name]

    def qty_setter(instance, value):
        if value > 0:
            instance.__dict__[storage_name] = value
        else:
            raise ValueError("value must be > 0")

    return property(qty_getter, qty_setter)


class LineItem:
    weight = quantity('weight')  # 使用特性工厂函数定义weight类属性
    price = quantity('price')  # price 属性

    def __init__(self, description, weight, price):
        self.description = description
        self.weight = weight  # 激活属性，确保不为负数和0
        self.price = price

    def subtotal(self):
        return self.weight * self.price  # 使用特性中存储的值


line1 = LineItem("name1", 8, 13.5)
print(line1.weight, line1.price)  # 8 13.5
print(sorted(vars(line1).items()))


# [('description', 'name1'), ('price', 13.5), ('weight', 8)]


class BlackKnight:
    def __init__(self):
        self.members = ['an arm',
                        'another arm',
                        'a leg',
                        'another leg']
        self.phrases = ["'Tis but a scratch.",
                        "It's just a flesh wound.",
                        "I'm invincible!",
                        "All right, we'll call it a draw."]
    @property
    def member(self):
        print("next member is:")
        return self.members[0]
    @member.deleter
    def member(self):
        text = 'BLACK KNIGHT (loses {})\n-- {}'
        print(text.format(self.members.pop(0), self.phrases.pop(0)))

knight = BlackKnight()
print(knight.member)
# next member is:
# an arm
del knight.member
# BLACK KNIGHT (loses an arm)
# -- 'Tis but a scratch.
del knight.member
# BLACK KNIGHT (loses another arm)
# -- It's just a flesh wound.
del knight.member
# BLACK KNIGHT (loses a leg)
# -- I'm invincible!
del knight.member
# BLACK KNIGHT (loses another leg)
# -- All right, we'll call it a draw.
# del knight.member
# IndexError: pop from empty list