class Dog:

    # this method gets called whenever a new object is created
    # the purpose of __init__ is to initilise or assign values to object/instance
    # self is basically "this"
    # self is the instance
    def __init__(self, name, color):  # also called Dunder (Double Underscore)
        # print(f"Inside Init: {self}")
        self.name = name
        self.color = color
        print("Object created....")


d1 = Dog("Bruno", "Brown")  # when you do this , __init__ gets called

print(d1.name)

d2 = Dog("lily", "red")

print(d2.name)
# print(f" Outside: {d1}")
'''
Dog() -> this call does three things.
>> create and assigns memory for the new objects
>> passes it on to init
>> it also returns the same address
'''
