"""
    If the word's length in string is greater than 8 then make it 8 and if it contains any postfix('st', 'ly', 'ing' and
    'ed') remove those from word
"""
li = ['ed', 'ing', 'ly', 'st']


def trim_str(s):
    li1 = s.split(' ')
    result = ' '
    for i in range(0, len(li1)):
        if len(li1[i]) > 8:
            li1[i] = li1[i][:8]
        else:
            for j in li:
                if li1[i].endswith(j):
                    li1[i] = li1[i].rstrip(j)
    result = result.join(li1)
    return result


x = 'a boy is happing extremest'
res = trim_str(x)
print(res)
