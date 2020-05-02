class A:
    def __init__(self):
        self.a = 42
    
    def message(msg):
        self.msg = msg

a = A()
# print(a.a)

# a.b = 32
# print(a.b)

# a.message('Hello')
# print(a.msg)

class A:
    def __init__(self):
        self.a = 42

class B:
    def __init__(self):
        self.a = 47

class C(A,B):
    def __init__(self):
        super().__init__()
        print (self.a)

# c = C()


