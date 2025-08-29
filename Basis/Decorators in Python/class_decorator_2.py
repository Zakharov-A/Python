
def my_decorator_class(cls):
    class MyCls:

        def __init__(self, *args, **kwargs):
            self._obj = cls(*args, **kwargs)


        def __getattribute__(self, s):
            try:
                # check if this an attribute of the MyCls
                x = super().__getattribute__(s)
            except AttributeError:
                # no
                pass
            else:
                # yes this is attribute of the MyCls
                return x
            # try to call the object attribute
            attr = self._obj.__getattribute__(s)
            # is it a method
            if isinstance(attr, type(self.__init__)):
                # yes
                print("Call method: ", attr)
                return attr
            else:
                # not a method
                print("value: ", attr)
                return attr
            
    return MyCls

@my_decorator_class
class Person:
    def __init__(self, name):
        self.name = name
        self.__age = 0

    def set_age(self, value):
        self.__age = value

    def get_age(self):
        print(self.__age)


person = Person('John')
person.get_age()
person.set_age(25)
person.get_age()
print(person.name)