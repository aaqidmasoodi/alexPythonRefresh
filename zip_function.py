items = ["milk", "cheese", "cherry", "pepper"]
prices = ["2.49", "3.12", "4.12", "8.7"]
discounts = ["50%", "75%", "20%", "10%"]

# zip will return tuples and that is getting assinged into "item"
for item in zip(items, prices, discounts):
    print(item)


# here since there are 2 or more variables
# there is unpacking happening

# for item, price, discount in zip(items, prices, discounts):
#     print(f"ITEM={item}, PRICE={price}, DISCOUNT={discount}")
