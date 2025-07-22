class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Cat(Animal):
    def mau(self):
        print('Mau-mau')    


class Dog(Animal):
    def __init__(self, lastname, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.lastname = lastname

    def gav(self):
        print('Gav-gav')


cat = Cat('Bob', 2)
print(cat.name, cat.age)

dog = Dog('John', 'Wick', 3)
print(dog.name, dog.lastname, dog.age)
dog.gav()

dog2 = Dog(name = 'Bobik', lastname='Lee', age = 4)
print(dog2.name, dog2.lastname)