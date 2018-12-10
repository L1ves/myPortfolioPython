def get_formatted_name(first_name, last_name, middle_name = ''):
    """Возвращает аккуратно отформатированное полное имя."""
    if middle_name:
        full_name = first_name + ' ' + middle_name + ' ' + last_name
    else:
        full_name = first_name + ' ' + last_name
    return full_name.title()
musician = get_formatted_name('jimi', 'hendrix')
print(musician)

musician = get_formatted_name('john', 'hooker', 'lee')
print(musician)

def build_person(first_name, last_name):
    person = {'first' : 'first_name', 'last' : 'last_name'}
    return person
musician = build_person('jack', 'jackiel')
print(musician)

def build_person(first_name, last_name, age = ''):
    person = {'first' : 'first_name', 'last' : 'last_name'}
    if age:
        person['age'] = age
    return person
musician = build_person('jack', 'jackiel', age=21)
print(musician)


def get_formatted_name(first_name, last_name):
    full_name = first_name + ' ' + last_name
    return full_name.title()
while True:
    print("\nPlease tell me your first name: ")
    print("\nOr insert quit for exit")
    f_name = input("First name: ")
    if f_name == 'quit':
        break
    print("\nPlease tell me your last name: ")
    print("\nOr insert quit for exit")
    l_name = input("Last name: ")
    if l_name == 'quit':
        break
    formatted_name = get_formatted_name(f_name, l_name)
    print("\nHello " + formatted_name)

#def get_formatted_name(first_name, last_name):
#    return full_name.title()
#while True:
#    print("\nPlease tell me your name: ")
#    formatted_name = get_formatted_name(f_name, l_name)
    #print("\nHello " + formatted_name + "!")
def city_country(city, country):
    c_country = city + ', ' + country
    return c_country.title()
city_count = city_country('Moskow', 'Russia')
print(city_count)
city_count = city_country('Pekin', 'China')
print(city_count)
city_count = city_country('Kazahstan', 'Astana')
print(city_count)

def make_album(author_album, album_songs, track = ''):
    author_album = {'author' : author_album, 'album' : album_songs}
    if author_album:
        author_album['track'] = track
        return author_album
while True:
    print("\nInsert name album or author")
    print("Insert q for quit")
    answer = input("\nInsert your choise:")
    first = make_album('Viktor Tscoi', 'Kino',track=3)
    print(first)
    second = make_album('Malchishnik', 'Klava', track=7)
    print(second)
    third = make_album('Mr.robot', 'Main theme', track=5)
    print(third)
    if answer == 'q':
        break
    if answer == 'a':
        print(first)
