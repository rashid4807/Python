class Point:
    def __init__(self, param1, param2 = None) -> None:
       if param2 is None and isinstance(param1,tuple) and len(param1) == 2 :
          if isinstance (param1[0],int) and isinstance(param1[1],int):
                 self._init_with_tuple(param1)
                 self.x = param1[0]
                 self.y = param2[1]
       elif isinstance(param1,int) and isinstance(param2, int):
           self.x = param1
           self.y = param2
       else:
           raise TypeError('Wrong types for point')           
    def _init_with_integers(self,x,y):
       self.x = x
       self.y = y

            
p1 = Point(4,5)
print(p1.x)
print(p1.y)
p2 = Point((7,8))
print(p2.x)
print(p2.y)

p3 = Point()