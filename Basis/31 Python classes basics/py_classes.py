class Animal:
    def __init__(self, name, age, health=100, damage=0):
        self.name = name
        self.__age = age
        self.health = health
        self.damage = damage

    def set_name(self, value):
        self.name = value

    def get_name(self):
        print(self.name)

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        if value <= 10:
            self.__age = value    

    def __str__(self):
        return f"Name - {self.name}, age - {self.__age}"     

    def set_damage(self):
        return self.damage
    
    def get_damage(self, value):
        self.health -= value

class Cat(Animal):
    def mau(self):
        print('Mau-mau')

    def get_damage(self, value):
        super().get_damage(value)
        print(f"Maauuu; Health = {self.health}")        


class Dog(Animal):
    def __init__(self, lastname, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.lastname = lastname

    def gav(self):
        print('Gav-gav')

    def get_damage(self, value):
        super().get_damage(value)
        print(f"Aaauuu; Health = {self.health}")    


cat = Cat('Bob', 2, damage=10)
dog = Dog('John', 'Wick', age=1, damage=15)

dog.gav()
cat.get_damage(dog.set_damage())
cat.mau()
dog.get_damage(cat.set_damage())


