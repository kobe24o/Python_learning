from urllib.request import urlopen
import warnings
import os
import json

URL = 'http://www.oreilly.com/pub/sc/osconfeed'
JSON = './osconfeed.json'


def load():
    if not os.path.exists(JSON):
        msg = 'downloading {} to {}'.format(URL, JSON)
        warnings.warn(msg)  # 发出提醒
        with urlopen(URL) as remote, open(JSON, 'wb') as local:
            # 使用两个上下文管理器
            local.write(remote.read())
            # 读取和保存远程文件
    with open(JSON) as fp:
        return json.load(fp)


feed = load()
print(feed)
print(sorted(feed['Schedule'].keys()))
for key, value in sorted(feed['Schedule'].items()):
    print('{:3} {}'.format(len(value), key))
print(feed['Schedule']['speakers'][-1]['serial'])
# 这种句法太长了。。。如何改进

from collections import abc


class FrozenJSON:
    # 一个只读接口，使用属性表示法访问JSON类对象
    def __init__(self, mapping):
        self.__data = dict(mapping)

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
