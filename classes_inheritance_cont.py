class Animal:

    def speak(self):
        print("Animal is speaking....")

    def walk(self):
        print("Animal is walking...")


class Dog(Animal):
    pass


class Cat(Animal):

    # overloading
    def speak(self):
        print("Cat is speaking...")


a1 = Animal()
d1 = Dog()
c1 = Cat()

print(dir(a1))

a1.speak()
d1.speak()
c1.speak()


# METHOD RESOLUTION ORDER
# FIRST OWN CLASS IS CHECKED >> IF NOT THERE >>> THEN IT WILL GO TO THE PARENT >> IF NOT THERE >> CHECK WHETHER IT IS A BUILTIN IN PYTHON >> IF NOT >>> THEN RAISE ERROR
