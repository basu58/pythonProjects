def rev_list(li):
    start, end = 0, len(li) - 1
    while start < end:
        li[start], li[end] = li[end], li[start]
        start += 1
        end -= 1


li = [1, 2, 3, 4, 5, 6]
rev_list(li)
print(li)
