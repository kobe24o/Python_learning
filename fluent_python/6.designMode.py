from abc import ABC, abstractmethod
from collections import namedtuple

Customer = namedtuple("Customer", "name fidelity")  # 顾客，积分


class LineItem:
    def __init__(self, product, quantity, price):
        self.product = product
        self.quantity = quantity
        self.price = price

    def total(self):
        return self.price * self.quantity


class Order:
    def __init__(self, customer, cart, promotion=None):
        self.customer = customer
        self.cart = list(cart)
        self.promotion = promotion

    def total(self):
        if not hasattr(self, '__total'):
            self.__total = sum(item.total() for item in self.cart)
        return self.__total

    def due(self):
        if self.promotion is None:
            discount = 0
        else:
            discount = self.promotion.discount(self)
        return self.total() - discount

    def __repr__(self):
        fmt = '<Order total: {:.2f} due: {:.2f}>'
        return fmt.format(self.total(), self.due())


class Promotion(ABC):  # 策略的抽象基类
    @abstractmethod
    def discount(self, order):
        """返回折扣金额"""


class FidelityPromo(Promotion):  # 第一个具体策略
    def discount(self, order):
        return order.total() * 0.05 if order.customer.fidelity >= 1000 else 0


class BulkItemPromo(Promotion):  # 第二个具体策略
    def discount(self, order):
        discount = 0
        for item in order.cart:
            if item.quantity >= 20:
                discount += item.total() * 0.1
        return discount


class LargeOrderPromo(Promotion):  # 第三个具体策略
    def discount(self, order):
        distinct_items = {item.product for item in order.cart}
        if len(distinct_items) >= 10:
            return order.total() * 0.07
        return 0


joe = Customer("John Doe", 0)
ann = Customer("Ann Smith", 1100)
cart = [LineItem('banana', 4, 0.5),
        LineItem('apple', 10, 1.5),
        LineItem('watermelon', 5, 5.0)]
print(Order(joe, cart, FidelityPromo()))
# <Order total: 42.00 due: 42.00>
print(Order(ann, cart, FidelityPromo()))  # 积分超过1000,95折
# <Order total: 42.00 due: 39.90>
banana_cart = [LineItem('banana', 30, .5),
               LineItem('apple', 10, 1.5)]
print(Order(joe, banana_cart, BulkItemPromo()))  # 超过20件的打9折
# <Order total: 30.00 due: 28.50>
long_order = [LineItem(str(item_code), 1, 1.0)
              for item_code in range(10)]
print(Order(joe, long_order, LargeOrderPromo()))  # 不同的种类数 >= 10, 93折
# <Order total: 10.00 due: 9.30>
print(Order(joe, cart, LargeOrderPromo()))
# <Order total: 42.00 due: 42.00>


# 使用函数实现 策略
Customer = namedtuple("Customer", "name fidelity")  # 顾客，积分


class LineItem:
    def __init__(self, product, quantity, price):
        self.product = product
        self.quantity = quantity
        self.price = price

    def total(self):
        return self.price * self.quantity


class Order:
    def __init__(self, customer, cart, promotion=None):
        self.customer = customer
        self.cart = list(cart)
        self.promotion = promotion

    def total(self):
        if not hasattr(self, '__total'):
            self.__total = sum(item.total() for item in self.cart)
        return self.__total

    def due(self):
        if self.promotion is None:
            discount = 0
        else:
            discount = self.promotion(self)
        return self.total() - discount

    def __repr__(self):
        fmt = '<Order total: {:.2f} due: {:.2f}>'
        return fmt.format(self.total(), self.due())


def FidelityPromo(order):  # 第一个具体策略
    return order.total() * 0.05 if order.customer.fidelity >= 1000 else 0


def BulkItemPromo(order):  # 第二个具体策略
    discount = 0
    for item in order.cart:
        if item.quantity >= 20:
            discount += item.total() * 0.1
    return discount


def LargeOrderPromo(order):  # 第三个具体策略
    distinct_items = {item.product for item in order.cart}
    if len(distinct_items) >= 10:
        return order.total() * 0.07
    return 0


joe = Customer("John Doe", 0)
ann = Customer("Ann Smith", 1100)
cart = [LineItem('banana', 4, 0.5),
        LineItem('apple', 10, 1.5),
        LineItem('watermelon', 5, 5.0)]
print(Order(joe, cart, FidelityPromo))
# <Order total: 42.00 due: 42.00>
print(Order(ann, cart, FidelityPromo))  # 积分超过1000,95折
# <Order total: 42.00 due: 39.90>
banana_cart = [LineItem('banana', 30, .5),
               LineItem('apple', 10, 1.5)]
print(Order(joe, banana_cart, BulkItemPromo))  # 超过20件的打9折
# <Order total: 30.00 due: 28.50>
long_order = [LineItem(str(item_code), 1, 1.0)
              for item_code in range(10)]
print(Order(joe, long_order, LargeOrderPromo))  # 不同的种类数 >= 10, 93折
# <Order total: 10.00 due: 9.30>
print(Order(joe, cart, LargeOrderPromo))
# <Order total: 42.00 due: 42.00>

a = globals()
# {'__name__': '__main__', '__doc__': None, '__package__': None,
# '__loader__': <_frozen_importlib_external.SourceFileLoader object at 0x0000020E89A9C340>,
# '__spec__': None, '__file__': 'D:/gitcode/Python_learning/fluent_python/6.designMode.py', '__builtins__': <module 'builtins' (built-in)>, '_pydev_stop_at_break': <function _pydev_stop_at_break at 0x0000020E8E17D160>,
# 'ABC': <class 'abc.ABC'>, 'abstractmethod': <function abstractmethod at 0x0000020E89AB2CA0>,
# 'namedtuple': <function namedtuple at 0x0000020E89BE6CA0>, 'Customer': <class '__main__.Customer'>,
# 'LineItem': <class '__main__.LineItem'>, 'Order': <class '__main__.Order'>, 'Promotion': <class '__main__.Promotion'>,
# 'FidelityPromo': <function FidelityPromo at 0x0000020E8FBEF0D0>, 'BulkItemPromo': <function BulkItemPromo at 0x0000020E8FBEFA60>, 'LargeOrderPromo': <function LargeOrderPromo at 0x0000020E8FBEFAF0>,
# 'joe': Customer(name='John Doe', fidelity=0), 'ann': Customer(name='Ann Smith', fidelity=1100), 'cart': [<__main__.LineItem object at 0x0000020E8FBF8190>, <__main__.LineItem object at 0x0000020E8FBF8280>, <__main__.LineItem object at 0x0000020E8FBF8310>], 'banana_cart': [<__main__.LineItem object at 0x0000020E8FBEACA0>, <__main__.LineItem object at 0x0000020E8FBEA6D0>], 'long_order': [<__main__.LineItem object at 0x0000020E8FBD9B80>, <__main__.LineItem object at 0x0000020E8FBEAE50>, <__main__.LineItem object at 0x0000020E8FBEAD30>, <__main__.LineItem object at 0x0000020E8FBF8370>, <__main__.LineItem object at 0x0000020E8FBF83D0>, <__main__.LineItem object at 0x0000020E8FBF8430>, <__main__.LineItem object at 0x0000020E8FBF8490>, <__main__.LineItem object at 0x0000020E8FBF84F0>, <__main__.LineItem object at 0x0000020E8FBF8550>, <__main__.LineItem object at 0x0000020E8FBF85E0>], 'a': {...}, 'promos': [<function FidelityPromo at 0x0000020E8FBEF0D0>, <function BulkItemPromo at 0x0000020E8FBEFA60>, <function LargeOrderPromo at 0x0000020E8FBEFAF0>],
# 'best_Promo': <function best_Promo at 0x0000020E8FBEFB80>}
promos = [globals()[name] for name in globals()
          if name.endswith('Promo') and name != "best_Promo"]
# 选择最佳折扣
def best_Promo(order):
    return max(promo(order) for promo in promos)
print("ok")