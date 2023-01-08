name = "Alex"
gender = "male"
state = "wisconsin"
phone_number = 754644

# 4 ways to format stuff in python
# auto type casts and type hints
# METHOD 1
print("Hi my name is", name, "i am a", gender,
      "i am from", state, "my phone:", phone_number)

# METHOD 2
print("my name is " + str(phone_number) + "i am a " + gender)

# METHOD 3
print("my name is {} and i am a {} and my phone is {}.".format(
    gender, name, phone_number))

# F-String | INDUSTRY STANDARD
print(
    f"FFF- My name is {name} and i am a {gender} and my phone is {phone_number}")
