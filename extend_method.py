# there are no hard datatype in python
# python lists are slow
# numpy arrays 10 .001

numbers = [5, 7, 8, 4]
print(id(numbers))

print(numbers[1])
# numbers.append([4, 8, 7, 5])
# extend will iterate over and then add one by one
# numbers.extend([4, 8, 7, 9])  # the object must be an iterable (loop over it) (collection)
numbers.append("Hello")
print(len(numbers))
print(numbers)
