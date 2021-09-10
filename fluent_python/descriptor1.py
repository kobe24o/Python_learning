class Quantity:
    __counter = 0  # Quantity 类属性，统计实例数量

    def __init__(self):
        cls = self.__class__  # cls 是 Quantity 类的引用
        prefix = cls.__name__ # 'Quantity'
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
        if value > 0:
            setattr(instance, self.storage_name, value)
        else:
            raise ValueError("value must be greater than 0")

    def __get__(self, instance, owner):
        if instance is None:
            return self
        return getattr(instance, self.storage_name)


class LineItem:
    weight = Quantity() # '_Quantity#0'
    # 描述符实例绑定给 weight 属性， 类属性，所有 LineItem实例共享
    price = Quantity()   # '_Quantity#1'

    def __init__(self, description, weight, price):
        self.description = description
        self.weight = weight
        self.price = price

    def subtotal(self):
        return self.weight * self.price


coconuts = LineItem('Brazilian coconut', 20, 17.95)
print(coconuts.weight, coconuts.price)
print(getattr(coconuts, '_Quantity#0'), getattr(coconuts, '_Quantity#1'))
print(LineItem.weight)
# 这种调用方式
# 描述符的 __get__ 方法接收到的 instance 参数值是 None
# AttributeError: 'NoneType' object has no attribute '_Quantity#0'