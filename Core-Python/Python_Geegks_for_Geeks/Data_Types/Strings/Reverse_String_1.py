def rev_str(s):
    str1 = ""
    for i in s:
        str1 = i + str1
    return str1


s = "Superb"

print("Reverse of String s is: ", rev_str(s))
