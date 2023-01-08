# Method resolution Order

# FIRST THE INSTANCE / OWN CLASS
# PARENT
# OBJECT / PYTHON BUILTIN

class A:

    def fun1(self):
        print("Print A")

    def speak(self):
        print("A is Speaking...")


class B:

    def fun2(self):
        print("Print B")

    def speak(self):
        print("B is Speaking...")


class C:

    def fun3(self):
        print("Print C")

    def speak(self):
        print("C is Speaking...")


class D(A, B, C):
    pass


d1 = D()

d1.speak()
print(D.__mro__)

d1.fun2()
