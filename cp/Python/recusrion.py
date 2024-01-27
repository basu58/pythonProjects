# finding factorials
def fact(num):
    if num == 0 or num == 1:
        return 1
    else:
        return num * fact(num - 1)


res = fact(int(input("Please enter a number to find factorial:")))
print(res)

"""print fibonacci series f0 = 0 f1 = 1 f2 = f1 + f0 fn = fn-1 + fn-2 using recursion here is not a good solution it 
will consume lots of memory and time to give the output. Here we can use iterator instead of that """


def recr(num):
    if num < 0:
        print("Invalid")
    elif num == 0:
        return 0
    elif num == 1:
        return 1
    else:
        return recr(num - 1) + recr(num - 2)


def itr(num):
    pn = 0
    cn = 1
    for i in range(1, num):
        ppn = pn
        pn = cn
        cn = ppn + pn
    return cn


result = recr(int(input("Please enter a number to find fibonacci:")))
print(result)
result = itr(int(input("Please enter a number to find fibonacci:")))
print(result)
