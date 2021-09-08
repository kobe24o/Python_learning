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
print(vars(obj)) # {}, vars 函数返回 obj 的 __dict__ 属性
print(obj.data) # class data attr
obj.data = "changed"
print(vars(obj)) # {'data': 'changed'}
print(Class.data) # class data attr
# 实例修改了data，但是 类属性没有被修改

print(Class.prop) # <property object at 0x0000021A91E4A680>
print(obj.prop) # prop value
# obj.prop = "changed prop"  # 报错 can't set attribute
obj.__dict__["prop"] = "changed prop1"
print(vars(obj)) # {'data': 'changed', 'prop': 'changed prop1'}
print(obj.prop) # prop value #
# 读取 obj.prop 时仍会运行特性的读值方法。特性没被实例属性遮盖
Class.prop = "haha" # 覆盖 Class.prop 特性，销毁特性对象
print(obj.prop) # changed prop1
# 现在，obj.prop 获取的是实例属性。
# Class.prop 不是特性了，因此不会再覆盖 obj.prop。

print(obj.data) # changed
print(Class.data) # class data attr
Class.data = property(lambda self : "data prop value")
# 使用新特性覆盖 Class.data
print(obj.data) # data prop value
# obj.data 被 Class.data 特性遮盖了
del Class.data # 删除特性
print(obj.data) # changed
# 恢复原样，obj.data 获取的是实例属性 data