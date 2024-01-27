# self represents the instance of the class. By using the “self”  we can access the attributes and
# methods of the class in python. It binds the attributes with the given arguments
# it is clearly seen that self and obj is referring to the same object
class Test:
    def __init__(self):
        print('Value of self = ', id(self))


obj = Test()

print('Value of obj', id(obj))


class Car:
    def __init__(self, model, color):
        self.model = model
        self.color = color

    def show(self):
        print('Car model is ', self.model)
        print('Car color is ', self.color)


obj1 = Car('Audi A4', 'Red')
obj2 = Car('BMW', 'White')

obj1.show()
obj2.show()

# Self is the first argument to be passed in Constructor and Instance Method.
