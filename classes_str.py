class Employee:

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    # this must return a string
    # changing the string represention of an object
    '''
        useful in django admin
    '''

    def __str__(self):
        return self.name


e1 = Employee("Patrick", "2000")
e2 = Employee("Robin", "3000")

print(e1)  # representing the object as a string
print(e2)
