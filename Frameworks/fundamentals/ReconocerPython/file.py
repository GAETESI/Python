num1 = 42 #variable declaration, number initialized
num2 = 2.3#variable declaration, decimal/float initialized
boolean = True#Data Types, Boolean
string = 'Hello World' # variable declaration, string initialized

#variable declaration, list
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives'] 

#variable declaration, dictionary
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False}

#variable declaration,Tuples
fruit = ('blueberry', 'strawberry', 'banana')

# print to console, type check
print(type(fruit))

# print to console, List access value
print(pizza_toppings[1])

#list add value
pizza_toppings.append('Mushrooms')

#print to console, Dictionary access value
print(person['name'])

#print to console, Dictionary access value
person['name'] = 'George'

# Dictionary change value
person['eye_color'] = 'blue'

# print to console, Tuple access data
print(fruit[2])

# Conditional if, evaluation, print to console, Conditional else, print to console
if num1 > 45: 
    print("It's greater")
else:
    print("It's lower")

# Conditional if - elif - else, print to console.
if len(string) < 5:
    print("It's a short word!")
elif len(string) > 15:
    print("It's a long word!")
else: 
    print("Just right!")

# For Loop start at 0 and goes up to until 5
for x in range(5): 
    print(x) 
 
# For Loop start at 2 and goes up to until 5   
for x in range(2,5):
    print(x)
    
# For loop start at 2 goes up to until 10, increments by 3    
for x in range(2,10,3):
    print(x)
    
#While Loop, variblae declaration    
x = 0 
while(x < 5): 
    print(x)# printing to console
    x += 1 # incrementing x

pizza_toppings.pop()# list delete last value
pizza_toppings.pop(1)# # list delete value at index

# print to console of dictionary
print(person)

# Dictionary delete value
person.pop('eye_color') 

#print to console of dictionary
print(person)

# for loop through a list
for topping in pizza_toppings: 
    if topping == 'Pepperoni':#conditional if
        continue #continue
    print('After 1st if statement')  # print to console
    if topping == 'Olives':
        break # break the loop

# function declaration
def print_hello_ten_times():
    for num in range(10): # for loop starts at 0 goes up until 10
        print('Hello')# print to console

print_hello_ten_times() # Function Call

def print_hello_x_times(x): # function Declaration with parameter x
    for num in range(x):# For loop up until a given number x
        print('Hello')# print to console

print_hello_x_times(4) # function call arguement of 4

def print_hello_x_or_ten_times(x = 10):# function declaration with default parameter
    for num in range(x):# For loop until x
        print('Hello')# print to console

print_hello_x_or_ten_times()# Function call goes to 10
print_hello_x_or_ten_times(4)# Function call goes to 4


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