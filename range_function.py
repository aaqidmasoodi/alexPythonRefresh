#              ST,SP,STEP
# for i in range(50, 100, 2):
#     print(i)

# continue - simply skip "this (current) iteration"
# break - Just simply break out of the loop
# EVEN NUMBERS upto 100
# for i in range(1, 100, 2):
#     print(i)
#     if i > 50:
#         break

# print numbers from 0 to 50 but skip numbers from 20-25 inclusive

for i in range(50):
    # if i > 20 and i < 25:
    if 20 <= i <= 25:
        continue  # Op code
    print(i)
