# An integer assignment
age = 45

# A floating point
salary = 1456.8

# A string
name = "John"

print(age)
print(salary)
print(name)

# declaring the var
Number = 100

# display
print(Number)

# declaring the var
Number = 100

# display
print("Before declare: ", Number)

# re-declare the var
Number = 120.3

print("After re-declare:", Number)

a = b = c = 10

print(a)
print(b)
print(c)

a, b, c = 1, 20.2, "Basudev"

print(a)
print(b)
print(c)

a = 10
a = "Basudev"

print(a)

a = 10
b = 20
print(a + b)

a = "Basu"
b = "Dev"
print(a + b)


# a = 10
# b = "Geeks"
# print(a+b) # unsupported operand type(s) for +: 'int' and 'str'

# This function uses local variable s
def f():
    s = "Welcome To Python"
    print(s)


f()


# This function uses a global variable
def f():
    print(s)


# Global scope
s = "I love India"
f()

# Python program to modify a global
# value inside a function

x = 15


def change():
    # using a global keyword
    global x

    # increment value of a by 5
    x = x + 5
    print("Value of x inside a function :", x)


change()
print("Value of x outside a function :", x)

# numberic
var = 123
print("Numeric data : ", var)

# Sequence Type
String1 = 'Welcome to the Python World'
print("String with the use of Single Quotes: ")
print(String1)

# Boolean
print(type(True))
print(type(False))

# Creating a Set with
# the use of a String
set1 = set("Basudev")
print("\nSet with the use of String: ")
print(set1)

# Creating a Dictionary
# with Integer Keys
Dict = {1: 'Geeks', 2: 'For', 3: 'Geeks'}
print("\nDictionary with the use of Integer Keys: ")
print(Dict)

#  Shared Reference
x = 5
y = x

