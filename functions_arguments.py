# keyword arguments
# positional arguments
def sum(a, b, c, d):
    print(f"value of a: {a}")
    print(f"value of b: {b}")
    print(f"value of c: {c}")
    print(f"value of d: {d}")
    return a + b + c + d


# print(sum(5, 7, 4, 9))  # passin arguments positionally
# print(sum(c=5, a=2, 4, 7))  # passin arguments using keywords
print(sum(4, 7, c=5, d=8))  # passin arguments using keywords

# this is not a problem and is seen a lot in production code
print("Hello", end="")
