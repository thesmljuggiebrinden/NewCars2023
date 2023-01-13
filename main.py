import random

class Vehicle:
    def __init__(self, make, model, year, color, body_styles, trim_lines,
                 drive_wheels, seating, engines, transmissions,
                 length, width, height, wheelbase, weight,
                 max_load, cargo_volume, towing_capacity,
                 fuel_type, mpg):
        self.make = make
        self.model = model
        self.year = year
        self.color = color
        self.body_styles = body_styles
        self.trim_lines = trim_lines
        self.drive_wheels = drive_wheels
        self.seating = seating
        self.engines = engines
        self.transmissions = transmissions
        self.length = length
        self.width = width
        self.height = height
        self.wheelbase = wheelbase
        self.weight = weight
        self.max_load = max_load
        self.cargo_volume = cargo_volume
        self.towing_capacity = towing_capacity
        self.fuel_type = fuel_type
        self.mpg = mpg

    def describe(self):
        print('A {} {} {} {}'.format(self.color, self.year, self.make, self.model))
        print('----------------------------------------------------------------')

    def overview(self):
        print('Body Styles: {}'.format(self.body_styles))
        print('Trim Lines: {}'.format(self.trim_lines))
        print('Drive Wheels: {}'.format(self.drive_wheels))
        print('Seating: {}'.format(self.seating))
        print('Engines: {}'.format(self.engines))
        print('Transmissions: {}'.format(self.transmissions))
        print('-----------------------------------------------')

    def dimensions(self):
        print('Length: {} in.'.format(self.length))
        print('Width: {} in.'.format(self.width))
        print('Height: {} in.'.format(self.height))
        print('Wheelbase: {} in.'.format(self.wheelbase))
        print('Weight: {} lb.'.format(self.weight))
        print('-------------------------------------')

    def cargo(self):
        print('Max Load: {} lb.'.format(self.max_load))
        print('Cargo Volume: {} cu.Ft.'.format(self.cargo_volume))
        print('Towing Capacity: {} lb.'.format(self.towing_capacity))
        print('-------------------------------------------------')

    def fuel(self):
        print('Fuel Type: {}'.format(self.fuel_type))
        print('{} mpg'.format(self.mpg))
        print('-------------------------')

    def distance(self, miles):
        self.gallons = miles / self.mpg
        print("To go {} miles, the {} {} {} {} gets {} gallons.".format(miles, self.color, self.year, self.make,
                                                                            self.model, self.gallons))


class Smart(Vehicle):
    pass

class Acura(Vehicle):
    pass

class AlfaRomeo(Vehicle):
    pass

class Audi(Vehicle):
    pass

class BMW(Vehicle):
    pass

class Buick(Vehicle):
    pass

class Cadillac(Vehicle):
    pass

class Chevrolet(Vehicle):
    pass

class Chrysler(Vehicle):
    pass

class Dodge(Vehicle):
    pass

class Fiat(Vehicle):
    pass

class Ford(Vehicle):
    pass

class Genesis(Vehicle):
    pass

class GMC(Vehicle):
    pass

class Honda(Vehicle):
    pass

class Hyundai(Vehicle):
    pass

class Infiniti(Vehicle):
    pass

class Jaguar(Vehicle):
    pass

class Jeep(Vehicle):
    pass

class Kia(Vehicle):
    pass

class LandRover(Vehicle):
    pass

class Lexus(Vehicle):
    pass

class Lincoln(Vehicle):
    pass

class Lucid(Vehicle):
    pass

class Maserati(Vehicle):
    pass

class Mazda(Vehicle):
    pass

class MercedesBenz(Vehicle):
    pass

class Mini(Vehicle):
    pass

class Mitsubishi(Vehicle):
    pass

class Nissan(Vehicle):
    pass

class Polestar(Vehicle):
    pass

class Porsche(Vehicle):
    pass

class Ram(Vehicle):
    pass

class Rivian(Vehicle):
    pass

class Subaru(Vehicle):
    pass

class Tesla(Vehicle):
    pass

class Toyota(Vehicle):
    pass

class Volkswagen(Vehicle):
    pass

class Volvo(Vehicle):
    pass

smart = Smart('Smart', 'EQ ForTwo', 2019, 'white', 'Coupe', 'Pure', 'RWD', '2 front', 'Electric', '1-speed direct drive',  106, 75, 61, 73.7, 2373, 635, 8.9, 635, 'Electric', 108 )
smart.describe()
smart.overview()
smart.dimensions()
smart.cargo()
smart.fuel()

miles = int(input("Enter the number of miles"))

smart.distance(miles)

