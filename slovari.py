
alien_0 = {'color' : 'green'}
print(alien_0['color'])

alien_0 = {'color' : 'green', 'point' : 5}
print(alien_0['color'])
print(alien_0['point'])

new_points = alien_0['point']
print("You just earned " + str(new_points) + " points!")

alien_0 = {'color' : 'green', 'point' : 5}
print(alien_0)
alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)

alien_0 = {}
alien_0['color'] = 'green'
alien_0['point'] = 5
print(alien_0)

alien_0 = {'color' : 'green', 'point' : 5}
print("The alien is " + alien_0['color'] + ".")
alien_0['color'] = 'yellow'
print("The alien is now " + alien_0['color'] + ".")

alien_0 = {'x_position' : 0, 'y_position' : 25, 'speed' : 'medium'}
print("Original X position is: " + str(alien_0['x_position']))
#пришелец перемещается вправо
#вычисляем величину смещения на основании текущей скорости
if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
elif alien_0['speed'] == 'fast':
    x_increment = 4
#пришелец двигается быстро
else:
    x_increment = 3
# Новая позиция равна сумме старой позиции и приращения.
alien_0['x_position'] = alien_0['x_position'] + x_increment
print("New X position is: " + str(alien_0['x_position']) + ".")

alien_0 = {'color' : 'green', 'point' : '5'}
print(alien_0)
del alien_0 ['point']
print(alien_0)

favorite_language = {
    'jen' : 'python',
    'sarah' : 'c',
    'edward' : 'ruby',
    'phil' : 'python',
}
print("Sara'h favorite language is: " +
    favorite_language['sarah'].title() +
     ".")

duda = {
    'first_name' : 'anna',
    'last_name' : 'dudnikova',
    'age' : '22',
    'city' : 'tagil'
}
print(duda)

favorite_number = {
    'lev' : '333',
    'vita' : '111',
    'anton' : '999',
    'leonid' : '555',
    'maria' : '777',
}
print(favorite_number)

programing_language = {
    'if' : 'esli',
    'elif' : 'ili',
    'else' : 'togda',
    'and' : 'i',
    'for' : 'dlia',
}
print(programing_language['if'])
print(programing_language['elif'])
print(programing_language['else'])
print("\nI learn this word yesterday :\n\t " +
    programing_language['and'] +
    ".")
print("\nI love syntaxys :\n\t " +
    programing_language['for'].title() +
    ".")

user_0 = {
    'username' : 'efermi',
    'first' : 'enrico',
    'last' : 'fermi',
}


for key, value in user_0.items():
     print("\nKey: " + key)
     print("\nValue: " + value)

favorite_language = {
    'jen' : 'python',
    'sarah' : 'c',
    'edward' : 'ruby',
    'phil' : 'python',
}
for name, language in favorite_language.items():
    print(name.title() +
    "'s Favorite language is: " +
    language.title())

favorite_language = {
    'jen' : 'python',
    'sarah' : 'c',
    'edward' : 'ruby',
    'phil' : 'python',
}

for name in favorite_language.keys():
    print(name.title())

favorite_language = {
    'jen' : 'python',
    'sarah' : 'c',
    'edward' : 'ruby',
    'phil' : 'python',
}

friends = ['sarah', 'jen']
for name in favorite_language.keys():
    print(name.title())
    if name in friends:
        print("Hi! " + name.title() +
            " I see, you favorite language is :" +
            favorite_language[name].title() + "!")

favorite_languages = {
'jen': 'python',
'sarah': 'c',
'edward': 'ruby',
'phil': 'python',
}

if 'john'  not in favorite_languages.keys():
    print("John! Take oure pull!")

favorite_languages = {
'jen': 'python',
'sarah': 'c',
'edward': 'ruby',
'phil': 'python',
}

for name in sorted(favorite_languages.keys()):
    print(name.title() + " Thank you for talking the poll")

favorite_languages = {
'jen': 'python',
'sarah': 'c',
'edward': 'ruby',
'phil': 'python',
}
print("The following languages have been mentioned:")
for language in favorite_languages.values():
        print(language.title())

favorite_languages = {
'jen': 'python',
'sarah': 'c',
'edward': 'ruby',
'phil': 'python',
}
print("The following languages have been mentioned:")
for language in set(favorite_languages.values()):
    print(language.title())

programing_language = {
    'if' : 'esli',
    'elif' : 'ili',
    'else' : 'togda',
    'and' : 'i',
    'for' : 'dlia',
    'while' : 'lala',
    'python' : 'mylove',
    'white hat' : 'best hacker',
    'black hat' : 'bad hacker',
    'django' : 'web',
}
for language, content in programing_language.items():
    print("\nI learn this word yesterday : " +
    language + "\nI love syntaxys : " +
    content.title() +
    ".")

reaver = {
    'volga' : 'russia',
    'temza' : 'uk',
    'nil' : 'egyptian',
}
for reavers, country in reaver.items():
    print("\nThe "+
    reavers.title() +
    " runs through " + country.title() + ".")

reaver = {
    'volga' : 'russia',
    'temza' : 'uk',
    'nil' : 'egyptian',
}
for reavers, country in reaver.items():
    print(reavers.title())

reaver = {
    'volga' : 'russia',
    'temza' : 'uk',
    'nil' : 'egyptian',
}
for reavers, country in reaver.items():
    print(country.title())

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    'andrew' : 'c++',
    'olga' : 'go'
}
for name, language in programing_language.items():
    print("\nMy name is : " +
    language + "\nI love language: " +
    content.title() +
    ".")

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',

}
for name, values in favorite_languages.items():
    print("\nThank you " +
name +
" for your voice.")
new_member = ['andrew', 'olga']
if 'andrew' not in favorite_languages:
    print("Andrew, if you have already been interviewed")
if 'olga' not in favorite_languages:
    print("Olga, if you have already been interviewed")

alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}

aliens = [alien_0, alien_1, alien_2]
for alien in aliens:
    print(alien)

# Создание пустого списка для хранения пришельцев.
aliens = []
# Создание 30 зеленых пришельцев.
for alien_number in range(30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)
# Вывод первых 5 пришельцев:
for alien in aliens[:5]:
    print(alien)
print("...")
print("Total number of aliens: " + str(len(aliens)))

# Создание пустого списка для хранения пришельцев.
aliens = []
# Создание 30 зеленых пришельцев.
for alien_number in range(0,30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)
for alien in aliens[0:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10
        print(alien)
    print("...")

# Сохранение информации о заказанной пицце.
pizza = {
'crust' : 'thick',
'toppings' :['mushrooms', 'extra cheese'],
}
# Описание заказа
print("You ordered a : " + pizza['crust'] + "-crust pizza" +
    " with the following toppings")
for topping in pizza['toppings']:
    print("\t" + topping)

favorite_languages = {
'jen': ['python', 'ruby'],
'sarah': ['c'],
'edward': ['ruby', 'go'],
'phil': ['python', 'haskell'],
}
for name, languages in favorite_languages.items():
        print("\n" + name.title() + "'s favorite languages are:")
        for language in languages:
            print("\t" + language.title())

users = {
'aenstein' : {
    'first' : 'albert',
    'last' : 'enstein',
    'location' : 'princetone',
    },
'mcurie' : {
    'first' : 'marie',
    'last' : 'curie',
    'location' : 'paris',
    },
}
for username, user_info in users.items():
    print("\nUsername: " + username)
    full_name = user_info['first'] + " "+ user_info['last']
    location = user_info['location']
    print("\nFull name " + full_name.title() + ".")
    print("\nLocation " + location.title() + ".")

people = {
    'duda' : {
        'first_name' : 'anna',
        'last_name' : 'dudnikova',
        'age' : '22',
        'city' : 'tagil',
        },
    'leva' : {
        'first_name' : 'lev',
        'last_name' : 'makeev',
        'age' : '26',
        'city' : 'tagil',
        },
    'anton' : {
        'first_name' : 'anton',
        'last_name' : 'nerush',
        'age' : '29',
        'city' : 'tagil',
        },
}
print(people)

numbers = {
    'lev' : '777',
    'anton' : '333',
    'vita' : '555',
}
for name, number in numbers.items():
    print("\n" + name + " 's favorite number is: " + number)

pets_1 = {'breed' : 'english terrier','name' : 'butch','dog_owner' : 'miron'}
pets_2 = {'breed' : 'sheepdog','name' : 'jessie','dog_owner' : 'andrey'}
pets_3 = {'breed' : 'chihuahua','name' : 'chichi','dog_owner' : 'denis'}
pets = [pets_1,pets_2,pets_3]
print(pets_1)
print(pets)

favorite_places = {
    'anton' : ['gym','street','park'],
    'lev' : ['maryj','gym'],
    'vita' : ['home'],
}
for name, places in favorite_places.items():
    print("\n" + name.title() + " favorite place is: ")
    for place in places:
        print("\t" + place.title())

favorite_number = {
    'lev' : ['333','222'],
    'vita' : ['111','444'],
    'anton' : ['999','888'],
    'leonid' : ['555','666'],
    'maria' : ['777','000'],
}
for friend, number in favorite_number.items():
    print("My friend " + friend.title() + " had lucky numbers:")
    for numbers in number:
        print("\t" + numbers)

cities = {
    'msk' : {
        'name' : 'moskow',
        'country' : 'russia',
        'population' : '9 mln',
        },
    'spb' : {
        'name' : 'saint petersburg',
        'country' : 'russia',
        'population' : '6 mln',
        },
    'ekb' : {
        'name' : 'ekaterinburg',
        'country' : 'russia',
        'population' : '2 mln',
    },
}
print(cities['msk'])
for info, cities_people in cities.items():
    print("\ncities " + info.title())
    live = cities_people['name'] + " " + cities_people['population'] + " " + " population in " + cities_people['country']
    print("People lives in " + live.title())
