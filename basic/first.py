
#Basic syntax
print('My name is Marzia')
print('o----')
print(' ||||')
print('*' * 10)
price = 10
print(price)

#how to take input
name = input(' What is your name ? ')
color = input(' What is your favourite color? ')
print(name, 'likes ' + color)

#calculating age
birth_year = input('Enter your birth year ')
print(type(birth_year))
age = 2024 - int(birth_year)
print(type(age))
print (age)

#converting weight
weight_in_pounds = input('Give your weight in pounds ')
weight_in_kg = int(weight_in_pounds) * 0.45
print('Your weight in kg is ', weight_in_kg)

#using parantheses '' "" 

print("Python's course for beginners")
print('python course for " Beginners"')

#multi line string

message = """ 
 here is the first 
 conversation with you

 Thankyou 
 the support team


"""
print(message)