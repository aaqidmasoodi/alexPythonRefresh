message = "Good Morning!"

print(message[5])
# slicing
# works for all indexed collection (string, lists, tuples)
# start:stop:step
print(message[0:3])
print(message[0:])
print(message[5:8])

# in python we have negative indicies also
print(message[-1])


# using the step
#         start:stop:step
print(message[0:5:2])


# negative
# by default it the step is 1 >>>>>>>>
# the step -1 indicate <<<<<<< direction and number indicate how many to skip
print(message[-1::-1])  # start from end going up to start in reverse direction

# print formatted
print(f"Message is reverse is: {message[-1::-1]}")
