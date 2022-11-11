x = []
if __name__ == '__main__':
    for _ in range(int(input())):
        name = input()
        score = float(input())
        y = [name, score]
        x.append(y)


def func(sub_li):
    sub_li.sort(key=lambda a: a[1])
    return sub_li


l1 = func(x)
l2 = l1[len(l1)-2]
s = l2[1]
l3 = []
for p in l1:
    if p[1] == s:
        l3.append(p)
l4 = func(l3)
print(l4)
