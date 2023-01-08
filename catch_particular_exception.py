'''
API CALLS...
DATABASE CONNECTION...
FILE OPENING...
some sensitive code involving user input...
'''

try:
    print("Hello there!")
    # print(name)
except ZeroDivisionError:  # catch only ZeroDivisionError
    print("you cannot divide by zero.")
except NameError:
    print("Undefined variable was printed.")
except:  # catches any type of exception
    print("Something went wrong!")
else:  # only runs when everything in the try block is good
    print("Everything good.")
finally:  # will always run whether or not anything goes wrong.
    print("closing connection object to database...")

print("Hello World")
