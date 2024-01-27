str1 = "Hello, I am Basudev"
print("Initial String is \"{}\"".format(str1))
str2 = "Dev"
str3 = str1.replace("Basudev", str2)
print(str3)

li = list(str1)
str4 = "a"
for i in li:
    if i == str4:
        x = li.index(i)
        li[x] = "P"
str5 = "".join(li)
print(str5)

li2 = list(str1)
li2[2] = "x"
str6 = "".join(li2)
print(str6)

str6 = str1[0:2]
str7 = str1[3:]
str8 = str6 + 'y' + str7
print(str8)

