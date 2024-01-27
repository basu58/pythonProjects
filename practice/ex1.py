import itertools

num_inputs = int(input())
user_inputs = input("").split()
user_inputs1 = [int(a) for a in user_inputs]
x = [None] * len(user_inputs1)
for i in itertools.count(start=1, ):
    for j in range(0, len(x)):
        x[j] = i
        # print(x[j])
    if sum(x) > sum(user_inputs1):
        break


print(x[0])
