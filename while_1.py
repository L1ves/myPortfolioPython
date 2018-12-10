curent_number = 1
while curent_number <= 5:
    print(cdd)
    curent_number += 1


prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "
message = ""
while message != 'quit':
    message = input(prompt)
print(message)
if message != 'quit':
    print(message)

prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "
active = True
while active:
    message = input(prompt)
    if message == 'quit':
        active = False
    else:
        print(message)


prompt = "\nPlease enter the name of a city you have visited:"
prompt += "\n(Enter 'quit' when you are finished.) "
while True:
    city = input(prompt)
    if city == 'quit':
        break
else:
    print("I'd love to go to " + city.title() + "!")

curent_number = 0
while curent_number < 10:
    curent_number += 1
    if curent_number %2 == 0:
        continue
    print(curent_number)
x = 1
while x <= 5:
    print(x)
    x += 1
# Бесконечный цикл!
#x = 1
#while x <= 5:
#    print(x)

pizza = "\nPlease insert youre topping"
pizza += " or press 'quit'"
print(pizza)
message = ""
while message != 'quit':
    message = input(pizza)
    print(message)

age = input("\nPlease insert youre age " )
age = int(age)
print(age)
if age <= 3:
    print("You cost on the ticket is: free!")
elif age >= 12:
    print("You cost on the ticket is: 15!")
else:
    print("You cost on the ticket is: $10")

pizza = "\nPlease insert youre topping"
pizza += " or press 'quit' "
print(pizza)
message = ""
active = message
active = True
while active != 'quit':
    active = input(pizza)
    print(message)
if active == 'quit':
    active = False
else:
    print(pizza)

x = 2
while x <= 5:
    print(cdd
