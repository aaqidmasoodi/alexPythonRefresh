'''
THINGS A LOOP HAS TO HAVE
usual use case of a while loop is for infinite loop
for user inputs as well
for validating user inputs as well
'''
# loop variable
# condition
# increment of the loop variable

# everything you do is manual
i = 0
while i <= 10:  # False
    # body
    if 4 <= i <= 8:
        i += 1
        continue
    print(i)
    i += 1
