# Using single quotes
str1 = 'Hello Python'
print(str1)
# Using double quotes
str2 = "Hello Python"
print(str2)

# Using triple quotes
str3 = '''''Triple quotes are generally used for  
    represent the multiline or 
    docstring'''
print(str3)

str = "HELLO"
print(str[0])
print(str[1])
print(str[2])
print(str[3])
print(str[4])
# It returns the IndexError because 6th index doesn't exist
# print(str[6])

# Given String
str = "BASUDEV"
# Start Oth index to end
print(str[0:])
# Starts 1st index to 4th index
print(str[1:5])
# Starts 2nd index to 3rd index
print(str[2:4])
# Starts 0th to 2nd index
print(str[:3])
# Starts 4th to 6th index
print(str[4:7])

str = 'BASUDEV'
print(str[-1])
print(str[-3])
print(str[-2:])
print(str[-4:-1])
print(str[-7:-2])
# Reversing the given string
print(str[::-1])
# IndexError: string index out of range
# print(str[-12])

'''Updating the content of the strings is as easy as assigning it to a new string. The string object 
doesn't support item assignment i.e., A string can only be replaced with new string since its content 
cannot be partially replaced. Strings are immutable in Python.

str = "HELLO"
str[0] = "h"
print(str) # TypeError: 'str' object does not support item assignment

str = "BASUDEV"  
del str[1] #TypeError: 'str' object doesn't support item deletion


str = "They said, "Hello what's going on?""  
print(str) # SyntaxError: invalid syntax

 '''

# using triple quotes
print('''They said, "What's there?"''')

# escaping single quotes
print('They said, "What\'s going on?"')

# escaping double quotes
print("They said, \"What's going on?\"")

str = "Hello"
str1 = " world"
print(str * 3)  # prints HelloHelloHello
print(str + str1)  # prints Hello world
print(str[4])  # prints o
print(str[2:4])  # prints ll
print('w' in str)  # prints false as w is not present in str
print('wo' not in str1)  # prints false as wo is present in str1.
print(r'C://python37')  # prints C://python37 as it is written
print("The string str : %s" % str)  # prints The string str : Hello

print("C:\\Users\\BASUDEV CHHOTARAY\\Python32\\Lib")
print("This is the \n multiline quotes")
print("This is \x48\x45\x58 representation")

# format() method

# Using {} braces
print('{} and {} are both relative'.format('DEV', 'SHANKAR'))

# Using Positional arguments
print('{1}s and {0}s are very tasty'.format('Banana', 'Apple'))

# Using keyword arguments
print('{a}, {b} and {c} are best friends.'.format(a='Dev', b='Narayan', c='Shankar'))

Integer = 10;
Float = 1.290
String = "Basudev"
print("Hi I am Integer ... My value is %d\nHi I am float ... My value is %f\nHi I am string ..."
      "My value is %s" % (Integer, Float, String))
