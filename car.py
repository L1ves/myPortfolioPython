class Car():
    def __init__(self,make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def descriptive_name(self):
        long_name = self.make + '' + self.model + '' + str(self.year)
        return long_name.title()

    def read_odometr(self):
        print('Odometer this car is ' + str(self.odometer_reading) + ' km')

    def update_odometr(self, mileage):
        self.odometer_reading = mileage


my_new_car = Car('audi ', 'a8 ', 2018)
print(my_new_car.descriptive_name())
#my_new_car.odometer_reading = 23
my_new_car.update_odometr(23)
my_new_car.read_odometr()
