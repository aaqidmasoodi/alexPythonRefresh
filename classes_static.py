class Developer:

    def __init__(self, name):
        self.name = name

    # instance methods
    # methods are just functions inside a class
    # we just call them method.. nothing special
    def change_name(self, new_name):
        self.name = new_name

    @staticmethod
    def get_time():  # when you define a parameter

        return "12-01-2023 11:59:12"


d1 = Developer("Aaqid")

time = d1.get_time()  # python will pass always the instance to the methods

print(time)
