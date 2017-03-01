# static method and class method
class MyClass():
    @staticmethod
    def foo(arg1, arg2):
        print(arg1, arg2)

    @classmethod
    def bar(cls, arg1):
        print(cls, arg1)

MyClass.foo(1,2)
MyClass.bar(3)

# property
class Person():
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

p1 = Person("John")
print(p1._name)
print(p1.name)
p1.name = "Mary"
print(p1.name)

