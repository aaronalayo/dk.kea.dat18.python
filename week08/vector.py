from math import hypot

class Vector:
    """ Euclidean vector in 2D.

    >>> v1 = Vector(2, 4)
    >>> v2 = Vector(2, 1)
    >>> v1 + v2
    Vector(4, 5)

    >>> v = Vector(3, 4)
    >>> abs(v)
    5.0

    >>> v * 3
    Vector(9, 12)
    >>> abs(v * 3)
    15.0

    >>> True if Vector(0, 0) else False
    False
    >>> True if Vector(1, 0) else False
    True
    """

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Vector({self.x}, {self.y})"

    def __abs__(self):
        return hypot(self.x, self.y)

    def __bool__(self):
        return bool(abs(self))

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)
v1 = Vector(2, 4)
v2 = Vector(2, 1)

v = Vector(3, 4)
print(abs(v))



v*3
print( abs(v * 3))

print(bool(v2))

# if __name__ == '__main__':
#     import doctest
#     doctest.testmod(verbose=True, optionflags=doctest.ELLIPSIS)