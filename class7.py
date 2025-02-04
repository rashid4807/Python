class MyClass:
    def my_method(self, parameter):
        if isinstance(parameter,int):
            return parameter +1
        elif isinstance(parameter, str):
            return parameter.capitalize() + '.'
        else:
            raise TypeError('parameter type not supported.')
        

my_object = MyClass()
print(my_object.my_method(10))
print(my_object.my_method('moi'))
