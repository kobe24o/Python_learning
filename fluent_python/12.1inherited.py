class AnswerDict(dict):
    def __getitem__(self, key):
        return 24


ad = AnswerDict(a="good")
print(ad['a'])  # 24
d = {}
d.update(ad)
print(d['a'])  # good
print(ad)  # {'a': 'good'}
print(d)  # {'a': 'good'}

import collections


class AnswerDict2(collections.UserDict):
    def __getitem__(self, key):
        return 24
ad = AnswerDict2(a="good")
print(ad['a'])  # 24
d = {}
d.update(ad)
print(d['a'])  # 24
print(ad)  # {'a': 'good'}
print(d)  # {'a': 24}