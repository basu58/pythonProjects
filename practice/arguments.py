def m2(**kwargs):
    for a in kwargs.items():
        print(a, end=" ")


class Test:
    def __init__(self):
        self.x = 10
        self.y = 20

    @staticmethod
    def m1(*args):
        for a in args:
            print(a, end=" ")


obj = Test()
for x in range(1, 6):
    Test.m1(x)
print()
Test.m1(1, 2, 3, 6, 55)
print()
li = [22, 11, 21, 12]
Test.m1(li)
print()
Test.m1(*li)
print()
dic = {'letters': 'xyz', 'phrase': 'galaxy'}
# Test.m3(*dic)
m2(a=10, b=20)
