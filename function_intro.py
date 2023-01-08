# def merge(list_1, list_2):
#     pass

x = None


# print("Hello")
# functions that do not explicitly return anything, by defualt return None


def greet():
    print("Good Morning!!")

    return 5


print(f"Directly printing function greet() -> {greet()}")

x = greet()  # this at the end of the call becomes whatever is returned from the function


print(f"value of x = {x}")
