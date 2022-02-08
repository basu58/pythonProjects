str = "Python"
for i in str:
    print(i)

li = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
n = 5
for i in li:
    c = n * i
    print(c)

li = [10, 30, 23, 43, 65, 12]
sum1 = 0
for i in li:
    sum1 = sum1 + i
print("The sum is:", sum1)

for i in range(10):
    print(i, end=' ')

n = int(input("Enter the number "))
for i in range(1, 11):
    c = n * i
    print(n, "*", i, "=", c)

n = int(input("Enter the number "))
for i in range(2, n + 1, 2):
    print(i)

list = ['Peter', 'Joseph', 'Ricky', 'Devansh']
for i in range(len(list)):
    print("Hello", list[i])

# User input for number of rows
rows = int(input("Enter the rows:"))
# Outer loop will print number of rows
for i in range(0, rows + 1):
    # Inner loop will print number of Asterisk
    for j in range(i):
        print("*", end='')
    print()

rows = int(input('Enter the rows: '))
# Outer loop will print number of rows
for i in range(0, rows + 1):
    # Inner loop will print number of Asterisk
    for j in range(i):
        print(i, end='')
    print()

for i in range(0, 5):
    print(i)
else:
    print("for loop completely exhausted, since there is no break.")

for i in range(0, 5):
    print(i)
    break
else:
    print("for loop is exhausted")
print("The loop is broken due to break statement...came out of the loop")


