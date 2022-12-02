#  can you inheritance for multiple animals instead one for dog and one for cat
class Pet:  # This is the super class / upper level parent class
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        print(f'I am {self.name} and I am {self.age} years old')

    def speak(self):
        print("I don't know what to say")


class Cat(Pet):
    def __init__(self, name, age, color):  # name and age still need to be called
        super().__init__(name, age)  # super references the super class (Pet)
        self.color = color  # name and age are the parameters

    def speak(self):
        print('Meow')

    def show(self):
        print(f'I am {self.name} and I am {self.age} years old and I am {self.color}')


class Dog(Pet):
    def speak(self):
        print('Bark')


class Fish(Pet):
    pass


p = Pet('Tim', 19)
p.show()
c = Cat('Bill', 34, 'Brown')
c.speak()
d = Dog('Jill', 25)
d.speak()
f = Fish('Bubbles', 10)
f.speak()  # there was no speak defined
