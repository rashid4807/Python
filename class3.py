from typing import Self
from math import sqrt

class Vector:
    def __init__(self,x:int|float, y: int|float):
        self.x = x
        self.y = y
    
    def __repr__(self) -> str:
        return f'Vector({self.x},{self.y})'


    def __eq__(self, other:Self)-> bool:
        if isinstance(other,Vector):
           return self.x == other.x and self.y == other.y
        return NotImplemented
    

    def __add__(self, other:Self)-> Self:
        if isinstance(other,Vector):
           return self.__class__(self.x + other.x , self.y + other.y)#self.__class__ == Vector
        return NotImplemented

    def __sub__(self, other:Self)-> Self:
        if isinstance(other,Vector):
           return Vector(self.x - other.x , self.y - other.y)#self.__class__ == Vector
        return NotImplemented
    def __neg__(self) -> 'Vector':
        return Vector(-self.x, -self.y)
    
    @property
    def length(self) -> float:
        return sqrt(self.x**2 + self.y**2)
    
    def __mul__(self,other: int|float) -> 'Vector':
       if isinstance(other,Vector) or isinstance(other, float):
          return Vector(self.x*other, self.y*other)  
       return NotImplemented  

    def __rmul__(self, other: int|float) -> 'Vector':
        return self.__mul__(other) 
    
    
v1 = Vector(2,3)
v2 = Vector(3,2)
v3 = Vector(2,3)
print(v1 == v2)
print(v1* 3.5)
#print(5 * v1)
print(v1.length)




