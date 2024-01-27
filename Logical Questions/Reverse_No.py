n = int(input("Enter a number:"))
Reverse = 0
while n != 0:
    Reverse = Reverse * 10 + n % 10
    n = (n // 10)
print(Reverse)