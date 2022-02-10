x = 'Apple'
y = 'Banana'
print('{} and {}'.format(x, y))
print('{1} and {0}'.format(y, x))

x = 10
print('Hexadecimal 10 = {0:x}'.format(x))
print('Decimal 10 = {0:d}'.format(x))
print('Binary 10 = {0:b}'.format(x))
print('Octal 10 = {0:o}'.format(x))

x, y = input("Enter two numbers:").split()
x = int(x)
y = int(y)



def unorganized(a, b):
    for i in range(a, b):
        print(i * 1, i ** 2, i ** 3, i ** 4)


def organized(a, b):
    for i in range(a, b):
        print('{:6d}{:6d}{:6d}{:6d}'.format(i * 1, i ** 2, i ** 3, i ** 4))


unorganized(x, y)
organized(x, y)

introduction = 'My name is {first_name} {second_name} aka {aka}.'
full_name = {
    'first_name': 'Basudev',
    'second_name': 'Chhotaray',
    'aka': 'Basu',
}

print(introduction.format(**full_name))

li = [10.36065326, 8.124345, 32.3454, 28.1829, 07.9209, 123.467598]


def trunc(q):
    for i in q:
        print('{:.2f}'.format(i))


trunc(li)
