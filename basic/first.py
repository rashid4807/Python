
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
#String and fstring
first = 'John'
last = 'Smith'
full_name = first + '[' + last + '] is a coder'
msg = f'{ first} {last} is a  beginner '
print(full_name)
print(msg)


#some methods for beginners
message1 = 'This is learning about methods'
print(message1.upper())
print(message1.replace('learning','practicing'))
print(message1.lower())
print(message1.title())
print(message1.find('learning'))
print(len(message1))
print('python' in message1)
print('learning' in message1)





