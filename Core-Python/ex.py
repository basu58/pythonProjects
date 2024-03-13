x = 'hello brother'
y = x.split(' ')
for i in range(0, len(y)):
    print(y[i])
    if 'h' in y[i]:
        y[i] = 'ddd'


print(' '.join(y))

print(x.rstrip('brother'))
print(len(x))

