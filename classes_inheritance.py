class Animal:

    def __init__(self, name, type):
        self.name = name
        self.type = type


class Dog(Animal):  # Dog is a subclass of Animal
    # This class is inheriting from the animal class.
    # pass
    def __init__(self, name, type, color):
        # call the parent call -->> whatever
        super().__init__(name, type)
        '''
        Otherwise you would have to repeat the same code.
            self.name = name
            self.type = type
        '''
        self.color = color


a1 = Animal("Tommy", "Land")
print(a1.name)

d1 = Dog("Lumo", "Land", "Brown")
print(d1.name)


# print(a1.name)
