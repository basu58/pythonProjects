"""a = 10
b = 0
print('a is dividing by Zero')
assert b != 0
print(a / b)"""


def my_func(a, b):
    c = a + b
    print(c)


my_func(10, 20)


class Myclass:
    x = 10

    def function_name(x):
        print(x)

    function_name(x)


a = 0
while a < 4:
    a += 1
    if a == 2:
        continue
    print(a)

for i in range(5):
    if i == 3:
        break
    print(i)
print("End of execution")

i = 18
if 1 < 12:
    print("I am less than 18")

n = 11
if n % 2 == 0:
    print("Even")
else:
    print("odd")

marks = int(input("Enter the marks:"))
if marks >= 90:
    print("Excellent")
elif 90 > marks >= 75:
    print("Very Good")
elif 75 > marks >= 60:
    print("Good")
else:
    print("Average")

a = 10
b = 12
del a
print(b)
# a is no longer exist
# print(a)

a = 0
try:
    b = 1 / a
except Exception as e:
    print(e)

'''a = 5
if a > 2:
    raise Exception('a should not exceed 2 ')'''

a = 0
b = 5
try:
    c = b / a
    print(c)
except Exception as e:
    print(e)
finally:
    print('Finally always executed')

li = [1, 2, 3, 4, 5]
for i in li:
    print(i)

a = 0
while a < 5:
    print(a)
    a = a + 1

import math

print(math.sqrt(25))

from math import sqrt

print(sqrt(25))

import calendar as cal

print(cal.month_name[5])

'''pass - The pass keyword is used to execute nothing or create a placeholder for future code. 
If we declare an empty class or function, it will through an error, so we use the pass keyword to declare 
an empty class or function.'''


class my_class:
    pass


def my_func():
    pass


def sum(a, b):
    c = a + b
    return c


print("The sum is:", sum(25, 15))

'''This keyword is used to check if the two-variable refers to the same object. It returns the true if they 
refer to the same object otherwise false. Consider the following example.'''

x = 5
y = 5

a = []
b = []
print(x is y)
print(a is b)


def my_func():
    global a
    a = 10
    b = 20
    c = a + b
    print(c)


my_func()

'''nonlocal - The nonlocal is similar to the global and used to work with a variable inside the nested 
function(function inside a function). Consider the following example.'''


def outside_function():
    a = 20

    def inside_function():
        nonlocal a
        a = 30
        print("Inner function: ", a)

    inside_function()
    print("Outer function: ", a)


outside_function()

'''The lambda keyword is used to create the anonymous function in Python. It is an inline function without a 
name. Consider the following example.'''

a = lambda x: x**2
for i in range(1,6):
  print(a(i))

''' yield - The yield keyword is used with the Python generator. It stops the function's execution and 
returns value to the caller. Consider the following example.'''


def fun_Generator():
    yield 1
    yield 2
    yield 3


# Driver code to check above generator function
for value in fun_Generator():
    print(value)

'''with - The with keyword is used in the exception handling. It makes code cleaner and more readable. 
The advantage of using with, we don't need to call close(). Consider the following example.'''

with open('file_path', 'w') as file:
    file.write('hello world !')

''' None - The None keyword is used to define the null value. It is remembered that None does not indicate 0,
false, or any empty data-types. It is an object of its data type, which is Consider the following example.'''

def return_none():
    a = 10
    b = 20
    c = a + b


x = return_none()
print(x)