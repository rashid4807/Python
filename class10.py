from functools import singledispatchmethod

class MyClass:
    @singledispatchmethod
    def my_method(self,value):
        print('Oletus methodi')

    @my_method.register(int)
    def my_method(self,value):
        print('Int -methodi')

    @my_method.register(str)
    def _(self,value):
        print('str-methodi')

my_object = MyClass()
my_object.my_method(10)
my_object.my_method('Moi')
my_object.my_method(2,'moi')