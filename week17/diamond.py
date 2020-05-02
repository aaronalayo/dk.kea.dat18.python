class A:
   def ping(self):
      print('ping:', self)


class B(A):
   def pong(self):
      print('pong:', self)


class C(A):
   def pong(self):
      print('PONG:', self)


class D(B, C):
   def ping(self):
      super().ping()
      print('post-ping:', self)

   def pingpong(self):
      self.ping()
      super().ping()
      self.pong()
      super().pong()
      C.pong(self)

from diamond import *
d = D()
print(d.pong())

print(C.pong(d))

# class A: pass

# class B: pass

# class C: pass

# class D(B, C):
#    def __init__(self):
#       print("MRO: ", self.__class__.__mro__)
#       for base in self.__class__.__bases__:
#             print("Base class: ", base)


# if __name__ == '__main__':
#    d = D()