class Developer:

    def __init__(self, name):
        self.name = name

    # instance methods
    # methods are just functions inside a class
    # we just call them method.. nothing special
    def change_name(self, new_name):
        self.name = new_name


d1 = Developer("Aaqid")
# in this syntax, python passes the instance automatically
d1.change_name("Alex")


# very discouraged syntax
# it defeats the purpose of OOP
Developer.change_name(d1, "Alex")

print(d1.name)
