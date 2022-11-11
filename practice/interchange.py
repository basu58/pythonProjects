l1 = [1, 2, 3, 4]
size = len(l1)
temp = l1[0]
l1[0] = l1[size - 1]
l1[size - 1] = temp
print(l1)
l1 = [1, 2, 5, 6]
l1[0], l1[-1] = l1[-1], l1[0]
print(l1)

