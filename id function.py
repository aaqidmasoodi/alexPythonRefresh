# the id function
my_list_1 = ["Hello", 5, 3, 8]
my_list_copy = my_list_1.copy()  # this doesn't actually make a copy
'''
line number 3 OP created a new list in the memory somewhere
'''


'''
    A method that gets called when an object is created.
    when Event Object is created i used the tigger to populate the secret code.
'''
# 20 mins - 30 mins
print("Printing Addressing...")
print(id(my_list_1))  # address function
print(id(my_list_copy))

# mutable - they can be changed
my_list_1[2] = 10

print(f"ORGINIGAL: {my_list_1}")
print(f"COPY: {my_list_copy}")
