def add(*args):  # usually called args the parameter
    # print(args)
    acc = 0
    for num in args:
        acc += num
    return acc


print(add(4, 5, 7, 4))
print(add(4, 5, 7, 4, 5, 7, 9, 4))


# in python we do not directly have function overloading
# so this wont work
# def add(x, y):
#     return x + y

# the latest definition only is remembered or called
# def add(x, y, z):
#     return x + y + z


# print(add(3, 4, 3))

# def sum_list(user_list):
#     total = 0
#     for item in user_list:
#         total += item  # accumilator

#     return total


# list_sum = sum_list([5, 8, 7, 6, 4, 2, 1])
# print(list_sum)
