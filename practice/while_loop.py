# prints all letters except 'a' and 'v'
import limit as limit

i = 0
str1 = 'Basudev'

while i < len(str1):
    if str1[i] == 'a' or str1[i] == 'v':
        i += 1
        continue
    print('Current Letter :', str1[i])
    i += 1

# The control transfer is transfered
# when break statement soon it sees t
i = 0
str1 = 'Basudev'

while i < len(str1):
    if str1[i] == 'a':
        i += 1
        break
    print('Current Letter :', str1[i])
    i += 1

# An empty loop
str1 = 'Basudev'
i = 0

while i < len(str1):
    i += 1
    pass
print('Value of i :', i)

i = 1
# The while loop will iterate until condition becomes false.
while i <= 10:
    print(i)
    i = i + 1

i = 1
number = 0
b = 9
number = int(input("Enter the number:"))
while i <= 10:
    print("%d X %d = %d \n" % (number, i, number * i))
    i = i + 1

'''var = 1
while var != 2:
    i = int(input("Enter the number:"))
    print("Entered value is %d" % i)'''

i = 1
while i <= 5:
    print(i)
    i = i + 1
else:
    print("The while loop exhausted")

i = 1
while i <= 5:
    print(i)
    i = i + 1
    if i == 3:
        break
else:
    print("The while loop exhausted")

terms = int(input("Enter the terms "))
# first two initial terms
a = 0
b = 1
count = 0

# check if the number of terms is Zero or negative
if terms <= 0:
    print("Please enter a valid integer")
elif terms == 1:
    print("Fibonacci sequence up to:")
    print(a, b)
else:
    print("Fibonacci sequence:")
    while count < terms:
        print(a, end=' ')
        c = a + b
        # updating values
        a = b
        b = c
        count += 1
