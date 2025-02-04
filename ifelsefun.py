list = ["a","b" ,"c"]
list1 = []
if list:
    print('List has elements')
else: 
    print("List is empty")
    
a = 0
b = 5
c = 7
if (a == 5 and b ==6) or c == 0:
  print (True)
else:
   print("nothing matched")
if a == 5 and (b ==6 or c == 7):
  print(False)
else:
   print("This data is not also matched")

i = 1
while i < 6:
 print(i)
 i+=1

a = 6
match a:
  case 5:
    print("Viisi")
  case 6:
    print("kuusi")
  case _:
      print("enything else")

d = 5
e = 5

if d > e:
    print ("d is greater than e")
elif d == e:
    print("d is equal  to e")


 
  