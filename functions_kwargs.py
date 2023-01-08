# this allows a function to accept any number of keyword arguments
def generate_secret(code, user, **kwargs):
    print("hello")
    # all the kwargss
    print(kwargs)


generate_secret("gbf783", "alex", car="Hello", bike="yo!", new_var="234")
