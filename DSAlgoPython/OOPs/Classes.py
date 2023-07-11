# what is an object?
# what is a class

# when we are defining anything we define the instance of an object

#method called with .operator

class Dog(object):
    def __init__(self, name):
        self.name = name
        print('Nice you made a dog')

    def speak(self):
        pass
        print("Hi, I am", self.name)
    # attributes are variables that belong to a specific class  

tim = Dog('Tim')
tim.speak()