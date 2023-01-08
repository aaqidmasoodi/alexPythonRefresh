class Dog:
    pass


my_dog = Dog()  # this is called the constructor of the class
# print(type(my_dog))

# create variables in the instrance
# you do not even have the name varible in the class but
# still you can dynamically (at run time) create the variable
my_dog.name = "Bruno"
my_dog.color = "brown"

print(my_dog.name)

my_dog2 = Dog()
my_dog2.name = "lily"
my_dog2.color = "white"

print(my_dog2.color)

# printing the name space
print(my_dog.__dict__)
print(my_dog2.__dict__)


print(my_dog)
print(my_dog2)

'''
OOP Princple - MUST FOLLOW
'''
# DRY - Don't Repeat yourself
