def func():
    command = input().split(' ')
    arr = []
    if command[0] == 'append':
        arr.append(int(command[1]))
    elif command[0] == 'insert':
        arr.insert(int(command[2]), int(command[1]))
    elif command[0] == 'remove':
        arr.remove(int(command[1]))
    elif command[0] == 'pop':
        arr.pop(int(command[1]))
    elif command[0] == 'reverse':
        arr.reverse()
    elif command[0] == 'sort':
        arr.sort()
    else:
        print(arr)


if __name__ == '__main__':
    N = int(input())
    print(N)
    for i in range(0, N):
        func()
