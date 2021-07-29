class Foo:
    def __getitem__(self, pos):
        return range(0, 30, 10)[pos]


f = Foo()
print(f[1])  # 10
for i in f:
    print(i)  # 0, 10, 20
# 如果没有 __iter__ 和 __contains__ 方法，
# Python 会调用 __getitem__ 方法，
# 设法让迭代和 in 运算符可用

import collections

Card = collections.namedtuple('Card', ['rank', 'suit'])


class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits for rank in self.ranks]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]

    def __setitem__(self, key, value):
        self._cards[key] = value

    def __str__(self):
        return ",".join(str(i) for i in self._cards)


# def set_card(deck, position, card):
#     deck._cards[position] = card
#
#
# FrenchDeck.__setitem__ = set_card

from random import shuffle

deck = FrenchDeck()
print(str(deck))
shuffle(deck)  # TypeError: 'FrenchDeck' object does not support item assignment
print(str(deck))


class Test:
    def __len__(self):
        return 24


from collections import abc

print(isinstance(Test(), abc.Sized)) # True
