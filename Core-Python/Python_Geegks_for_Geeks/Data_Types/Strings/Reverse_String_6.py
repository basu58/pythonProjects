def rev(s):
    s = [s[i] for i in range(len(s) - 1, -1, -1)]
    return "".join(s)


str1 = "Hello Basudev"
print(rev(str1))
