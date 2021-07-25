from array import array
import math


class Vector2D:
    typecode = 'd'  # 类属性

    def __init__(self, x, y):
        self.__x = float(x)
        self.__y = float(y)

    @property
    def x(self):
        return self.__x

    @property  # @property 装饰器把读值方法标记为特性
    def y(self):
        return self.__y

    @classmethod  # 装饰器， 函数不需要传入 self 参数，需要cls 传入类本身
    # classmethod 最常见的用途是 定义备选构造方法
    # @staticmethod 就是定义在类中的普通函数
    def frombytes(cls, octets):
        typecode = chr(octets[0])
        memv = memoryview(octets[1:]).cast(typecode)
        return cls(*memv)  # 构造类对象

    @staticmethod
    def hello():
        print("hello world!")

    def __iter__(self):  # 可迭代对象，才能拆包 x,y = my_vector
        return (i for i in (self.x, self.y))  # 生成器表达式

    def __repr__(self):
        class_name = type(self).__name__
        return '{}({!r},{!r})'.format(class_name, *self)
        # {!r} 获取 *self 的分量，可迭代对象

    def __str__(self):
        return str(tuple(self))  # 从可迭代对象生成元组

    # def __format__(self, fmt_spec=""):
    #     components = (format(c, fmt_spec) for c in self)
    #     # 使用内置的 format 把格式应用到各个分量上，构成一个可迭代的字符串
    #     return "({}, {})".format(*components) # 格式化字符串

    def angle(self):
        return math.atan2(self.y, self.x)

    def __format__(self, fmt_spec=""):
        if fmt_spec.endswith('p'):
            fmt_spec = fmt_spec[:-1]
            coords = (abs(self), self.angle())
            outer_fmt = "<{}, {}>"
        else:
            coords = self
            outer_fmt = "({}, {})"
        components = (format(c, fmt_spec) for c in coords)
        return outer_fmt.format(*components)

    def __bytes__(self):
        return (bytes([ord(self.typecode)]) + bytes(array(self.typecode, self)))

    def __eq__(self, other):
        return tuple(self) == tuple(other)

    def __abs__(self):
        return math.hypot(self.x, self.y)

    def __bool__(self):
        return bool(abs(self))

    def __hash__(self):
        return hash(self.x) ^ hash(self.y)


v1 = Vector2D(315687, 4)
print("test str {0.x:5.3e}".format(v1))
print(format(v1))  # (315687.0, 4.0)
print(format(v1, '.3f'))  # TypeError: unsupported format string passed to Vector2D.__format__

print(format(Vector2D(1, 1), 'p'))
print(format(Vector2D(1, 1), '.3ep'))
print(format(Vector2D(1, 1), '0.5fp'))
print(format(Vector2D(1, 1), '0.2f'))

# hash(v1) # TypeError: unhashable type: 'Vector2D'
v1.__x = 100
print(v1)  # (315687.0, 4.0)
# v1.x = 100 # AttributeError: can't set attribute
v2 = Vector2D(10, 20)
v3 = Vector2D(10, 20)
print(hash(v1))  # 315683
print(hash(v2))  # 30
print(v2 is v3)  # False
print(hash(v3))  # 30
print(set([v1, v2, v3]))  # {Vector2D(315687.0,4.0), Vector2D(10.0,20.0)}

print(v1.__dict__)  # {'_Vector2D__x': 315687.0, '_Vector2D__y': 4.0, '__x': 100}
print(v1._Vector2D__x)  # 315687.0
v1._Vector2D__x = 100
print(v1._Vector2D__x)  # 100
print(v1)  # (100., 4.0)

print(v1.typecode)  # d
print(v2.typecode)  # d
print(bytes(v1))  # b'd\x00\x00\x00\x00\x00\x00Y@\x00\x00\x00\x00\x00\x00\x10@'
print(Vector2D.typecode)  # d

v1.typecode = 'f'
print(v1.typecode)  # f
print(bytes(v1))  # b'f\x00\x00\xc8B\x00\x00\x80@'
print(Vector2D.typecode)  # d
v1.typecode = 'd'
print(v1.typecode)  # d

Vector2D.typecode = 'f'
print(Vector2D.typecode)  # f
print(v1.typecode)  # d
print(v2.typecode)  # f


class anOtherVec(Vector2D):
    typecode = 'f'

v4 = anOtherVec(3,4)
print(repr(v4))