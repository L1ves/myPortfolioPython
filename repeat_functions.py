def greet_users(name):
    """Выводит простое сообщение"""
    print("hello " + name + "!")
greet_users('jessie')
greet_users('jessie')
greet_users('irina')
greet_users('jessie')
greet_users('jessie')
greet_users('olia')


def display_function(main_theme):
    print(main_theme)
display_function('function')

def favorite_book(title):
    print(title)
favorite_book('One of my favorite books is Alice in Wonderland')

def home_pet(animal, name):
    print("My favorite animal is: " + animal + "\nHis name is: " + name.title() + ".")
home_pet('dog', 'butch')
home_pet('cat', 'j')

def greet_users(names):
    for name in names:
        msg = ("Hello " + name.title() + "!")
        print(msg)
usernames = ['hannah', 'ty', 'margot']
greet_users(usernames)

# Список моделей, которые необходимо напечатать.
unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []
# Цикл последовательно печатает каждую модель до конца списка.
# После печати каждая модель перемещается в список completed_models.
while unprinted_designs:
    current_design = unprinted_designs.pop()
    # Печать модели на 3D-принтере.
    print("Printing model: " + current_design)
    completed_models.append(current_design)
# Вывод всех готовых моделей.
print("\nThe following models have been printed:")
for completed_model in completed_models:
    print(completed_model)


def show_magician(magicians):
    for magician in magicians:
        magic = "Hello " + magician.title() + "!"
        print(magic)
magician1 = ['a', 'b', 'c', 'd']
show_magician(magician1)

def make_pizza(*toppings):
    print(toppings)
make_pizza('pepperoni')
make_pizza('mozarello', 'tomato', 'cheese')

def make_pizza(*toppings):
    print("\nMaking a pizza with the following toppings:")
    for topping in toppings:
        print("- " + topping)
make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')

def make_pizza(size, *toppings):
    print("\nMaking a " + str(size) +
    " -inch pizza with the following pizza :")
    for topping in toppings:
        print("- " + topping)
make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')



def sandwich(name, *toppings):
    print("\nMaking a " + (name) + " with toppings ")
    for topping in toppings:
        print(name + ' ' + topping)
sandwich('Colorado', 'bacon')
sandwich('bufallo', 'bacon', 'cheese', 'tomato')
sandwich('1', '2', '3', '4', '5' ,'6')

def build_profile(first, last, **user_info):
    """Строит словарь с информацией о пользователе."""
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key, value in user_info.items():
        profile[key] = value
    return profile
user_profile = build_profile('Evgeniy', 'Skvortsov', city=' Tagil',
                                    country='Russia',
                                     profession='cyber_detective')
print(user_profile)

def make_pizza(size, *toppings):
    print("\nMaking a " + str(size) +
    " -inch pizza with the following pizza :")
    for topping in toppings:
        print("- " + topping)
make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')
