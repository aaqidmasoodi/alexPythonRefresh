#            parameter
def greet(name="user", gender="male"):  # default parameter
    print(f"Hello {name}")
    print(f"You are a {gender}")


#     argument
print(greet("Alex"))
greet("Aaqid")
greet("Jenny", "female")
greet()
