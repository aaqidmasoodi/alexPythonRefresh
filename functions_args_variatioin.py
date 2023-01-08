def add(a, b, *args):  # this happens more than the other one
    acc = 0
    for num in args:
        acc += num
    return acc


print(add(1, 2, 3, 4, 5, 6, 7, 8, 9))
