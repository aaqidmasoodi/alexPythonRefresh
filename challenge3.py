num1 = int(input("Enter a number: "))
num2 = int(input("Enter another number: "))

try:
    print(f"Division of numbers: {num1/num2}")
except ZeroDivisionError:
    print("Opps! Divison by Zero not allowed.")
