players = ['lola', 'ola', 'krola', 'trola', 'ilola']
print(players[0:3])

players = ['lola', 'ola', 'krola', 'trola', 'ilola']
print(players[1:4])

players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[:4])

players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[4:])

players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[-3])

players = ['charles', 'martina', 'michael', 'florence', 'eli']
print("Here are the first three players on my team:")
for player in players[:3]:
    print(player.title())

my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]
print("My favorite foods a:")
print(my_foods)
print("\nFriend favorite foods a:")
print(friend_foods)

my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]
my_foods.append('ice cream')
friend_foods.append('apple')
print('my favorit foods a:')
print(my_foods)
print('My friend favorite foods a:')
print(friend_foods)

players = ['charles', 'martina', 'michael', 'florence', 'eli']
print("The first three items in the list are:")
print(players[:3])

players = ['charles', 'martina', 'michael', 'florence', 'eli']
print("The last three items in the list are:")
print(players[3:])

players = ['charles', 'martina', 'michael', 'florence', 'eli']
print("Three items from the midle of list are:")
print(players[1:3])

my_pizza = ['pepperoni', 'mozarella', 'cheese', 'meet', 'classic']
friend_pizza = my_pizza[:]
my_pizza.append('bacon')
print("My favorite pizza are:")
for pizzas in my_pizza[:]:
    print(pizzas.title())

friend_pizza.append('italiano')
print("\nfriend favorite pizza are:")
for friend_pizzas in friend_pizza[:]:
    print(friend_pizzas.title())

my_pizza = ['pepperoni', 'mozarella', 'cheese', 'meet', 'classic']
print(my_pizza)
friend_pizza = my_pizza[:]
my_pizza.append('bacon')
friend_pizza.append('italiano')
print("My favorite pizza are:")
print(my_pizza)
print("\nFriend favorite pizza are:")
print(friend_pizza)
