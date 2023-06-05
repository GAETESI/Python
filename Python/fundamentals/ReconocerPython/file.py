num1 = 42 #Data Types, Numbers
num2 = 2.3#Data Types, Numbers
boolean = True#Data Types, Boolean
string = 'Hello World'#Strings
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives'] #List
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False}#Dictionary
fruit = ('blueberry', 'strawberry', 'banana')#Tuples
print(type(fruit))#type check
print(pizza_toppings[1])#log statement
pizza_toppings.append('Mushrooms')#addvalue
print(person['name'])#log statement
person['name'] = 'George'#log statement
person['eye_color'] = 'blue'#log statement
print(fruit[2])#log statement

if num1 > 45: #conditional if
    print("It's greater")
else:#conditional else
    print("It's lower")

if len(string) < 5:#conditional if
    print("It's a short word!")
elif len(string) > 15:#conditional elif
    print("It's a long word!")
else: #conditional else
    print("Just right!")

for x in range(5): """for loop/ Range  #start
    print(x) #stop
for x in range(2,5):
    print(x)
for x in range(2,10,3):
    print(x)"""
x = 0 #variable declaration
while(x < 5): # while loop
    print(x)
    x += 1 

pizza_toppings.pop()# delete last value
pizza_toppings.pop(1)# delete value (1)

print(person) #log statement
person.pop('eye_color') #personError: name <eye_color> is not defined
print(person)#log statement

for topping in pizza_toppings: #function for
    if topping == 'Pepperoni':#conditional if
        continue #continue
    print('After 1st if statement') #sequence
    if topping == 'Olives':
        break # break

def print_hello_ten_times():#variable declaration
    for num in range(10): #for loop range-start
        print('Hello')

print_hello_ten_times() #log statement

def print_hello_x_times(x):#variable declaration
    for num in range(x):#for loop range-start
        print('Hello')

print_hello_x_times(4) #log statement

def print_hello_x_or_ten_times(x = 10):#variable declaration
    for num in range(x):#for loop range-start
        print('Hello')

print_hello_x_or_ten_times() #log statement
print_hello_x_or_ten_times(4) #log statement


"""
Bonus section
"""

# print(num3)
# num3 = 72
# fruit[0] = 'cranberry'
# print(person['favorite_team'])
# print(pizza_toppings[7])
#   print(boolean)
# fruit.append('raspberry')
# fruit.pop(1)