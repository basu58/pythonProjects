num = int(input("Enter a number to check:"))

flag = False

if num == 1:
    print('1 is not a prime number')
elif num > 1:
    for i in range(2, num):
        if(num % i == 0):
            flag = True
            break
    if flag:
        print("number is not a prime number")
    else:
        print(num,"is a prime number")

#
if all(num%i != 0 for i in range(2, num)):
    print('Prime number')