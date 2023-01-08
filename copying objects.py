my_list_1 = ["Hello", 5, 3, 8]

# my_list_copy = my_list_1  # this doesn't actually make a copy
my_list_copy = my_list_1.copy()  # this actually make a copy

# mutable - they can be changed
my_list_1[2] = 10

print(f"ORGINIGAL: {my_list_1}")
print(f"COPY: {my_list_copy}")
