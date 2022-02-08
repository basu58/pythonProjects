# single line string
text1 = 'hello'

# Multi-line string

text1 = 'hello\
        Text'
print(text1)

str2 = '''welcome  
to  
Python '''
print(str2)

x = 0b10100  # Binary Literals
y = 100  # Decimal Literal
z = 0o215  # Octal Literal
u = 0x12d  # Hexadecimal Literal

# Float Literal
float_1 = 100.5
float_2 = 1.5e2

# Complex Literal
a = 5 + 3.14j

print(x, y, z, u)
print(float_1, float_2)
print(a, a.imag, a.real)

# Boolean Literal

x = (1 == True)
y = (2 == False)
z = (3 == True)
a = True + 10
b = False + 10

print("x is", x)
print("y is", y)
print("z is", z)
print("a:", a)
print("b:", b)

# Special Literals

val1 = 10
val2 = None
print(val1)
print(val2)

# List

li = ['John', 678, 20.4, 'Peter']
li1 = [456, 'Andrew']
print(li)
print(li + li1)

# Dictionary

di = {'name': 'Pater', 'Age': 18, 'Roll_nu': 101}
print(di)

# Tuple

tup = (10, 20, "Dev", [2, 3, 4])
print(tup)

# Set

se = {'apple','grapes','guava','papaya'}
print(se)