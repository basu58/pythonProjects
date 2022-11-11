x = int(input())
A = {int(numbers) for numbers in input().split(' ', x - 1)}
y = int(input())
for y in range(0, y):
    op, size = input().split()
    size = int(size)
    A1 = {int(numbers) for numbers in input().split(' ', size - 1)}
    if op == 'intersection_update':
        A.intersection_update(A1)
    elif op == 'update':
        A.update(A1)
    elif op == 'symmetric_difference_update':
        A.symmetric_difference_update(A1)
    elif op == 'difference_update':
        A.difference_update(A1)

print(sum(A))