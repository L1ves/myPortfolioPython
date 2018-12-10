age = 17
if age >= 18:
    print("You are very old to vote!!!")
    print("Have you registered to vot yet?")
else:
     age <= 18
     print("Sorry you are too young for a vote!")
     print("Please register to vote as soon as you turn 18")

age = 12
if age < 4:
    print("You admission cost $0.")
elif age < 18:
     print("You admission cost is $5.")
else:
    print("You admission cost is $10.")

age = 12
if age < 4:
    price = 0
elif age < 18:
    price = 5
elif age < 65:
    price = 10
else:
    price = 5
print("You admission cost is $" + str(price) + ".")

age = 12
if age < 4:
    price = 0
elif age < 18:
    price = 5
elif age < 65:
    price = 10
elif age >= 65:
    price = 5
print("You admission cost is $" + str(price) + ".")
