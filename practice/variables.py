print("Basudev")
print(type("Basudev"))
a = 50
b = a
print(id(a))
print(id(b))
# Reassigned variable a
a = 500
print(id(a))

name = "Basudev"
age = 26
marks = 80.50

print(name)
print(age)
print(marks)

name = "A"
Name = "B"
naMe = "C"
NAME = "D"
n_a_m_e = "E"
_name = "F"
name_ = "G"
_name_ = "H"
na56me = "I"

print(name, Name, naMe, NAME, n_a_m_e, NAME, n_a_m_e, _name, name_, _name, na56me)

x = y = z = 50
print(x)
print(y)
print(z)

a, b, c = 5, 10, 15
print(a)
print(b)
print(c)


# Declaring a function
def add():
    # Defining local variables. They have scope only within a function
    a = 20
    b = 30
    c = a + b
    print("The sum is:", c)


# Calling a function
add()

# Declare a variable and initialize it
x = 101


# Global variable in function
def mainfunction():
    # printing a global variable
    global x
    print(x)
    # modifying a global variable
    x = 'Welcome To Python'
    print(x)


mainfunction()
print(x)

# Assigning a value to x
x = 6
print(x)
# deleting a variable.
# del x
print(x)

# A Python program to display that we can store
# large numbers in Python

a = 10000000000000000000000000000000000000000000
a = a + 1
print(type(a))
print(a)

# printing single value
a = 5
print(a)
print((a))

a = 5
b = 6
# printing multiple variables
print(a, b)
# separate the variables by the comma
print(1, 2, 3, 4, 5, 6, 7, 8)

str = "string using double quotes"
print(str)
s = '''A multiline 
string'''
print(s)

str1 = 'hello Basudev ' #string str1
str2 = ' how are you' #string str2
print(str1[0:2]) #printing first two character using slice operator
print(str1[4]) #printing 4th character of the string
print(str1*2) #printing the string twice
print(str1 + str2)# printing the concatenation of str1 and str2