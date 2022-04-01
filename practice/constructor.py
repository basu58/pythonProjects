class Test:
    def __init__(self):
        self.x = 10
        self.y = 20
        print(self.x, self.y, sep=" ")

    @staticmethod
    def m1():
        return 'Hello'

    def __del__(self):
        print("Test deleted...")


obj = Test()
print(Test.m1())
del obj
print(obj.m1())
