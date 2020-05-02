from array import array
import reprlib
import math
import numbers
import functools
import operator
import itertools


class Vector:
   """
      >>> v = Vector([1, 2, 3, 4])
      >>> list(v)
      [1.0, 2.0, 3.0, 4.0]
      >>> v = Vector((1, 2))
      >>> list(v)
      [1.0, 2.0]
      >>> v = Vector([3, 4, 5])
      >>> len(v)
      3
      >>> v[0], v[-1]
      (3.0, 5.0)
      >>> v7 = Vector(range(7))
      >>> v7[1:4]
      Vector([1.0, 2.0, 3.0])
      >>> v5 = Vector(range(5))
      >>> v5.x
      0.0
      >>> v5.y, v5.z, v5.t
      (1.0, 2.0, 3.0)
      >>> v1 = Vector([3, 4, 5])
      >>> v2 = Vector([6, 7, 8])
      >>> v1 + v2
      Vector([9.0, 11.0, 13.0])
      >>> v1 + v2 == Vector([3+6, 4+7, 5+8])
      True
      >>> v1 = Vector([3, 4, 5, 6])
      >>> v3 = Vector([1, 2])
      >>> v1 + v3
      Vector([4.0, 6.0, 5.0, 6.0])
      >>> v1 = Vector([3, 4, 5])
      >>> v1 + [10, 20, 30]
      Vector([13.0, 24.0, 35.0])
      >>> [10, 20, 30] + v1
      Vector([13.0, 24.0, 35.0])
      >>> v = Vector([0, 1, -2])
      >>> v * 3
      Vector([0.0, 3.0, -6.0])
      >>> 3 * v
      Vector([0.0, 3.0, -6.0])
      >>> v1 = Vector([1, 2, 3])
      >>> v2 = Vector([5, 6, 7])
      >>> v1 @ v2 == 38.0 # 1*5 + 2*6 +3*7
      True
      >>> v1 = Vector([1, 2, 3])
      >>> v2 = Vector([1, 2, 3])
      >>> v1 == v2
      True
      >>> v1 == (1, 2, 3)
      False
      >>> v1 == [1, 2, 3]
      False
   """

   typecode = 'd'
   shortcut_names = 'xyzt'

   def __init__(self, components):
      self._components = array(self.typecode, components)

   def __iter__(self):
      return iter(self._components)

   def __repr__(self):
      components = reprlib.repr(self._components)
      components = components[components.find('['):-1]
      return 'Vector({})'.format(components)

   def __str__(self):
      return str(tuple(self))

   def __bytes__(self):
      return (bytes([ord(self.typecode)]) +
               bytes(self._components))

   def __eq__(self, other):
      if isinstance(other, Vector):
            return len(self) == len(other) and all(a == b for a, b in zip(self, other))
      else:
            return NotImplemented

   def __hash__(self):
      hashes = (hash(x) for x in self._components)
      return functools.reduce(operator.xor, hashes, 0)

   def __abs__(self):
      return math.sqrt(sum(x * x for x in self))

   def __neg__(self):
      return Vector(-x for x in self)

   def __pos__(self):
      return Vector(self)

   def __bool__(self):
      return bool(abs(self))

   def __len__(self):
      return len(self._components)

   def __add__(self, other):
      try:
            pairs = itertools.zip_longest(self, other, fillvalue=0.0)
            return Vector(a + b for a, b in pairs)
      except TypeError:
            return NotImplemented

   def __radd__(self, other):
      return self + other

   def __mul__(self, scalar):
      if isinstance(scalar, numbers.Real):
            return Vector(n * scalar for n in self)
      else:
            return NotImplemented

   def __rmul__(self, scalar):
      return self * scalar

   def __matmul__(self, other):
      try:
            return sum(a * b for a, b in zip(self, other))
      except TypeError:
            return NotImplemented

   def __rmatmul__(self, other):
      return self @ other

   def __getitem__(self, index):
      cls = type(self)
      if isinstance(index, slice):
            return cls(self._components[index])
      elif isinstance(index, numbers.Integral):
            return self._components[index]
      else:
            raise TypeError(f'{cls.__name__} indices must be integers.')

   def __getattr__(self, name):
      cls = type(self)
      if len(name) == 1:
            pos = cls.shortcut_names.find(name)
            if 0 <= pos < len(self._components):
               return self._components[pos]
      raise AttributeError(f'{cls.__name__} object has no attribute {name}')

   def __setattr__(self, name, value):
      cls = type(self)
      if len(name) == 1:
            if name in cls.shortcut_names:
               error = f'Attribute {name} is read only.'
            elif name.islower():
               error = "Can't set attribute names 'a' to 'z' in {cls_name!r}"
            else:
               error = ''
            if error:
               msg = error.format(cls_name=cls.__name__)
               raise AttributeError(msg)
      super().__setattr__(name, value)

   @classmethod
   def frombytes(cls, octets):
      typecode = chr(octets[0])
      memv = memoryview(octets[1:]).cast(typecode)
      return cls(memv)


if __name__ == '__main__':
   import doctest
   doctest.testmod(verbose=True, optionflags=doctest.ELLIPSIS)