#Asignment 16
from collections import UserDict
# class DoppelDict(UserDict):
#    def __setitem__(self, key, value):
#       return super().__setitem__(key, [value] * 2)


# dd = DoppelDict(one=1)
# print(dd)
# dd = DoppelDict(one=2)
# print(dd)
# print("is it a dict?:", isinstance(dd, UserDict))

# class MyClass(UserDict):
#     pass

# data = MyClass(one=1,two=2)

# print(data)
# print("one:", data.get("one"))
# print("is it a dict?:", isinstance(data, UserDict))

class AnswerDict(UserDict):
   def __getitem__(self, key):
      return 42

ad = AnswerDict(a='foo')
print(ad['a'])
d = {}
d.update(ad)
print(d['a'])
print(d)
print("is it a dict?:", isinstance(d, dict))
