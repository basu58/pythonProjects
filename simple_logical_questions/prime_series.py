num1 = int(input("Enter the series starts from: "))
num2 = int(input("Enter the series ends at: "))
if num1 == 0 and num2 == 2:
    print("There is no prime number in between them.")
else:
    for i in range(num1, num2 + 1):
        flag = True
        if i == 1 or i == 0:
            continue
        for j in range(2, i):
            if i % j == 0:
                flag = False
                break
        if flag:
            print(f"{i} is prime number")
