class Test:
    a = 10
    b = 20
    def __init__(self):
        print("This is like class constructor in c++, java")
    # instance method : This will take atleast one arguments.
    def f1(self):
        print("Hello")
    # static method
    @staticmethod
    def f2(x,y):
        print(x,y)
    # class method
    @classmethod
    def f3(cls):
        print(cls)

t1 = Test()
# print(t1.f1())
# print(t1.a)

t2 = Test()
# print(t2.f2(12,21))
t3 = Test()
print(t3)