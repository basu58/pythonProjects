num = int(input("enter the number?"))
if num % 2 == 0:
    print("Number is even")

a = int(input("Enter a? "));
b = int(input("Enter b? "));
c = int(input("Enter c? "));
if a > b and a > c:
    print("a is largest");
if b > a and b > c:
    print("b is largest");
if c > a and c > b:
    print("c is largest");
if a == b and b == c and c == a:
    print('All numbers are same.')

age = int(input("Enter your age? "))
if age >= 18:
    print("You are eligible to vote !!");
else:
    print("Sorry! you have to wait !!");

num = int(input("enter the number?"))
if num % 2 == 0:
    print("Number is even...")
else:
    print("Number is odd...")

number = int(input("Enter the number?"))
if number == 10:
    print("number is equals to 10")
elif number == 50:
    print("number is equal to 50");
elif number == 100:
    print("number is equal to 100");
else:
    print("number is not equal to 10, 50 or 100");

marks = int(input("Enter the marks? "))
if 85 < marks <= 100:
    print("Congrats ! you scored grade A ...")
elif 60 < marks <= 85:
    print("You scored grade B + ...")
elif 40 < marks <= 60:
    print("You scored grade B ...")
elif 30 < marks <= 40:
    print("You scored grade C ...")
else:
    print("Sorry you are fail ?")


