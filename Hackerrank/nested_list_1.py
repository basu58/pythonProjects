li = []
if __name__ == '__main__':
    for _ in range(int(input())):
        name = input()
        score = float(input())
        li.append([name, score])
        li.sort()
        print(li)
