def rev(s):
    if len(s) == 0:
        return s
    else:
        return rev(s[1:]) + s[0]


str1 = "Hello Basudev"
print(rev(str1))
