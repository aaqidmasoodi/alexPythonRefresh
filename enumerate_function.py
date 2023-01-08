items = ["milk", "cheese", "cherry", "pepper"]
prices = ["2.49", "3.12", "4.12", "8.7"]

# this is useful pattern
for i in range(len(items)):
    print(f"INDEX = {i} - ITEM = {items[i]}")

for index, value in enumerate(items):
    # print(index, value)
    print(f"{value}-{prices[index]}")
