def greet_user():
    """Выводит простое приветствие."""
    print("Hello!")
greet_user()

def greet_user(username):
        """Выводит простое приветствие."""
        print("Hello " + username.title() + ".")
greet_user('Anna')

def display_message(function):
    print("\nThis chapter is very good :)" + function.title())
display_message('It is really cool!')

def favorite_book(little):
    print("\n" + little)
favorite_book('One of my favorite books is Alice ' +
'in Wonderland')

def describe_pet(animal_type, petname):
    print("\nI have a " + animal_type)
    print("\nMy " + animal_type + "'s name is " + petname.title() + ".")
describe_pet('elefant', 'jumbo')
describe_pet('dog', 'willie')

#describe_pet(animal_type='hamster', pet_name='harry')
#describe_pet(pet_name='harry', animal_type='hamster')

def make_shirt(size, text):
    print("\nThe size your tshirt is: " + size)
    print("\n The print on yor tshirt is :" + text)
make_shirt('XL', 'The world is mine!')

def make_shirt(size = 'XL', text = 'The world is mine!'):
    print("\nThe size your tshirt is: " + size)
    print("\nThe print on yor tshirt is :" + text)
make_shirt()


def make_shirt(size, text = 'The world is mine!'):
    print("\nThe size your tshirt is: " + size)
    print("\nThe print on yor tshirt is :" + text)
make_shirt('XL')

def make_shirt(size = 'L', text = 'I love python!'):
    print("\nSize is : " + size)
    print("\nText is: " + text)
make_shirt()

def make_shirt(text, size = 'L'):
    print("\nSize is : " + size)
    print("\nText is: " + text)
make_shirt('I love Python!')

def make_shirt(text, size = 'L'):
    print("\nSize is : " + size)
    print("\nText is: " + text)
make_shirt(text='I love Python!')

def descrybe_city(city, country = 'Russia'):
    print("\nI love " + country + " and my city " + city)
descrybe_city('Moskow')
descrybe_city('Saint-Petersburg')
descrybe_city('Ekaterinburg')
descrybe_city(city = 'Ufa')
