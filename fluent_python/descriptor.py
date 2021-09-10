class Quantity:
    def __init__(self, storage_name):
        self.storage_name = storage_name
        # storage_name 属性，
        # 这是托管实例中存储值的 属性的名称

    def __set__(self, instance, value):
        # self 是描述符 实例（即 LineItem.weight 或 LineItem.price）
        # instance 是 托管实例（LineItem 实例）
        if value > 0:
            instance.__dict__[self.storage_name] = value
            # 必须直接 处理托管实例的 __dict__ 属性；
            # 如果使用内置的 setattr 函数，
            # 会再次触发 __set__ 方法，导致无限递归
            # self.__dict__[self.storage_name] = value 错误写法
            #
        else:
            raise ValueError("value must be greater than 0")


class LineItem:
    weight = Quantity('weight')
    # 描述符实例绑定给 weight 属性， 类属性，所有 LineItem实例共享
    price = Quantity('price')

    def __init__(self, description, weight, price):
        self.description = description
        self.weight = weight
        self.price = price
    def subtotal(self):
        return self.weight * self.price

