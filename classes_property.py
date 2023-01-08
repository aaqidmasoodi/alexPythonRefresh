'''
the employee code of the employee should always be 
employee first name and followed by their age
EX: patrick Sunga 55
    patrick55
'''


class Employee:

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        # self.employee_code = f"{self.first_name}-{self.age}"

    def change_first_name(self, new_first_name):
        self.first_name = new_first_name

    def change_age(self, new_age):
        self.age = new_age

    @property  # dynamically getting values of the object
    def employee_code(self):

        return f"{self.first_name}-{self.age}"


e1 = Employee("Alex", "Sunga", 55)
print(e1.__dict__)
e2 = Employee("Aaqid", "Masoodi", 23)
# print(e2.__dict__)


print("Before changing name: ")
print(e1.employee_code)
print(e2.employee_code)

e1.change_first_name("Patrick")
print("After changing name: ")
# print(e1.__dict__)
# print(e2.__dict__)
print(e1.employee_code)
print(e2.employee_code)
