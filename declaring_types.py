# there are two ways of declating a python bultin type
# one way is by using a python literal
# another way is by using a constructor

x = 5
_x = int()
print(type(x))
print(type(_x))


x = 5.0
_x = float()
print(type(x))
print(type(_x))

x = []
_x = list()
print(type(x))
print(type(_x))

x = ()
_x = tuple()
print(type(x))
print(type(_x))

x = {}
_x = dict()
print(type(x))
print(type(_x))
