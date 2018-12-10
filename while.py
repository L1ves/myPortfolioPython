message = input("Tell me something, and i will repeat it back to you: ")
print(message)

name = input("Please input your name : ")
print("Hi, " + name + "!")

promt = "If you tell us who you are, we can personalize the messages you see."
promt += "\nWhat is your first name?"
name = input(promt)
print("\nHello, " + name + "!")

height = input("How tall are you, in inches? ")
height = int(height)
if height >= 36:
    print("\nYou're tall enough to ride!")
else:
    print("\nYou'll be able to ride when you're a little older.")

number = input("Enter a number, and I'll tell you if it's even or odd: ")
number = int(number)
if number %2 == 0:
    print("\nThe number " + str(number) + " is even.")
else:
    print("\nThe number " + str(number) + " is odd.")
drive_car = input("Hello mr, tell me, what car you need? ")
print(drive_car)
print(" Let me see if I can find you a Subaru")

table_reserved = input("Hello, please tell me how many seats do you want to book a table ")
table_reserved = int(table_reserved)
if table_reserved >= 8:
    print("\nSorry, but you have to wait")
else:
    print("Your table is ready")

number = input("Enter a number, and I'll tell you if it's multiple of 10: ")
number = int(number)
if number %10 == 0:
    print("\nThe number " + str(number) + " is multiple 10.")
else:
    print("\nThe number " + str(number) + " is not multiple 10.")
