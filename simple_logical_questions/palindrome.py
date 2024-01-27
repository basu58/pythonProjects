num = int(input('Enter a number'))
temp = num
rev = 0
while num > 0:
    div = num % 10
    rev = rev * 10 + div
    num = num // 10

if (temp == rev):
    print('palindrome')
else:
    print('Not a palindrome')

s1 = input('Enter a String:')


def pal(s):
    li = list(s)
    li.reverse()
    return "".join(li)


res = pal(s1)
if s1 == res:
    print('Palindrome')
else:
    print('Not a palindrome')
