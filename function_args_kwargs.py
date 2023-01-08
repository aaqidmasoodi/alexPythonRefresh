# the usefullness of this depends on the application
def my_fun(*args, **kwargs):
    print(args)
    print(kwargs["animal"])


my_fun(54, 54, 21, 3, animal="cat", gender="male")
