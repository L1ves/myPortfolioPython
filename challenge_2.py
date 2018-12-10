class Dog():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sit(self):
        '''собака садится'''
        print(self.name.title() + " is now sitting.")

    def roll_over(self):
        """Собака перекатывается по команде."""
        print(self.name.title() + " rolled over!")

my_dog = Dog('willie', 6)
print("My dog's name is " + my_dog.name.title() + ".")
print("My dog is " + str(my_dog.age) + " years old.")
my_dog.sit()
my_dog.roll_over()

your_dog = Dog('Lucy', 3)
print("\nYour dog's name is " + your_dog.name.title() + ".")
print("Your dog is " + str(your_dog.age) + " years old.")
your_dog.sit()
your_dog.roll_over()


class Restaurant():
    def __init__(self, restaurant_name,cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0


    def descrybe_restaraunt(self):
        print('Restaurant ' + self.restaurant_name + '-' + self.cuisine_type +
         ' is open, you are welcome!')

    def close_restaraunt(self):
        print('Restaurant ' + self.restaurant_name.title() + ' ' +
         self.cuisine_type.title() + ' is close')
#    def close(self):
#        print(self.restaurant_name + ' Restaurant is close, after 23 hours')
    def break_restaraunt(self):
        print('Restaraunt ' + self.restaurant_name.title() + ' ' +
         self.cuisine_type() + 'close on brake 14-15')


    def restaurant(self):
        print('Now guests in restaurant is ' + str(self.number_served) + '.')

    def guests_up(self,guest):
        self.number_served = guest

open_restaraunt = Restaurant('Vladimir', 'Putin')
open_restaraunt.descrybe_restaraunt()
#putin.open()

#putin.close()
close_restaraunts = Restaurant('backdor', 'stiller')
close_restaraunts.close_restaraunt()
#skvortsov.open()
#skvortsov.close()
break_restaraunts = Restaurant('backdor', 'stiller')
break_restaraunts.break_restaraunt

restaurants = Restaurant('',5)
restaurants.restaurant()


class User():
    def __init__(self, name, surname, age, town):
        self.name = name
        self.surname = surname
        self.age = age
        self.town = town


    def descrybe_user(self):
        print('This user ' + self.name.title() + ' ' + self.surname.title() +
         ' ' + str(self.age) + " year's old " + ' from ' +
          self.town.title() + '.')
alex = User('alex', 'baskov', 32, 'ekb')
alex.descrybe_user()
pasha = User('pasha', 'arkhipov', 26, 'n.tagil')
pasha.descrybe_user()
anton = User('anton', 'nerush', 30, 'sochi')
anton.descrybe_user()

class Car():
    def __init__(self, model, year, make):
        self.model = model
        self.year = year
        self.make = make
        self.odometr_reading = 0

    def descriptive_name(self):
        long_name = self.model + ' ' + self.make + ' ' + str(self.year)
        return long_name.title()

    def read_odometr(self):
        print('This car has ' + str(self.odometr_reading) + ' km')


    def update_odometr(self, mileage):
        self.odometr_reading = mileage

    def increment_odometer(self, miles):
        '''Увеличивает показания одометра с заданным приращением.'''
        self.odometr_reading += miles

my_car = Car('allroad', 2018, 'audi')
print('My car is ' + my_car.descriptive_name())

my_car.update_odometr(3500)
my_car.read_odometr()

my_car.increment_odometer(100)
my_car.read_odometr()
