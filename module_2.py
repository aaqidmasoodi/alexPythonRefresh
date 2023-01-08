print(f"module 2 name : {__name__}")


'''
    we use this to check if a module is run direclty
    and in that case we can run a specific piece of code.
    otherwise if this module were to imported in another module
    then this code will not run.
'''
if __name__ == "__main__":
    print("Hello world")
    print("Mary has a little lamb")
    print("Police")
