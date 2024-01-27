li = [1, 2, 3, 1, 2, 4, 8, 2, 9]
li1 = []
def replace_duplicates(li):
    for i in range(0, len(li)-1):
        for j in range(i+1, len(li)):
            if li[i] == li[j]:
                li1.append('x')
        else:
            li1.append(li[i])

    return li1

x = replace_duplicates(li)

print(li1)