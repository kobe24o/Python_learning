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
    def __new__(cls, arg):


    def __init__(self, mapping):
        self.__data = {}
        for k,v in mapping.items():
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
            return FrozenJSON.build(self.__data[name])

    @classmethod  # 备选构造方法，@classmethod 装饰器经常这么用
    def build(cls, obj):
        if isinstance(obj, abc.Mapping):
            return cls(obj)  # 构建 FrozenJSON
        elif isinstance(obj, abc.MutableSequence):
            # 是序列，对每个元素都进行 build
            return [cls.build(item) for item in obj]
        else:
            return obj


raw_feed = load()
feed = FrozenJSON(raw_feed)
print(len(feed.Schedule.speakers))
print(sorted(feed.Schedule.keys()))  # ['conferences', 'events', 'speakers', 'venues']
print(feed.Schedule.events[-1].name)  # Why Schools Don't Use Open Source to Teach Programming
p = feed.Schedule.events[-1]
print(type(p))  # <class '__main__.FrozenJSON'>
print(p.name)  # Why Schools Don't Use Open Source to Teach Programming
print(p.speakers)  # [157509]
# print(p.age)  # KeyError: 'age'


grad = FrozenJSON({'name': 'Jim Bo', 'class': 1982})
# print(grad.class) # invalid syntax
# print(getattr(grad, 'class')) # 1982
print(grad.class_)

grad = FrozenJSON({'2name': 'Jim Bo', 'class': 1982})
print(grad._2name) # SyntaxError: invalid syntax
