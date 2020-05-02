from array import array
import reprlib
import math


class Vector:
   """
      >>> v = Vector([1, 2, 3, 4])
      >>> list(v)
      [1.0, 2.0, 3.0, 4.0]
      >>> v = Vector((1, 2))
      >>> list(v)
      [1.0, 2.0]
   """

   typecode = 'd'

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
      return tuple(self) == tuple(other)

   def __abs__(self):
      return math.sqrt(sum(x * x for x in self))

   def __bool__(self):
      return bool(abs(self))
   
   def __len__(self):
        return len(self._components)

   def __getitem__(self, index):
        return self._components[index]



   @classmethod
   def frombytes(cls, octets):
      typecode = chr(octets[0])
      memv = memoryview(octets[1:]).cast(typecode)
      return cls(memv)


if __name__ == '__main__':
   import doctest
   doctest.testmod(verbose=True, optionflags=doctest.ELLIPSIS)
   v7 = Vector(range(7))
   print(v7[1:4])