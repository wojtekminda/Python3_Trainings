class Car(object):
    condition = "new"

    def __init__(self, model, color, Vmax):
        self.model = model
        self.color = color
        self.Vmax = Vmax

    def display_car(self):
        return "This is a %s %s with %s Vmax." % (self.color, self.model, self.Vmax)

    def drive_car(self):
        self.condition = "used"


class ElectricCar(Car):

    def __init__(self, model, color, Vmax, battery_type):
        self.model = model
        self.color = color
        self.Vmax = Vmax
        self.battery_type = battery_type

    def drive_car(self):
        self.condition = "like new"


my_car = Car("DeLorean", "silver", 100)
print(my_car.display_car())

print(my_car.condition)
my_car.drive_car()
print(my_car.condition)


my_electric_car = ElectricCar("Tesla", "red", 200, "molten salt")
print(my_electric_car.display_car())

print(my_electric_car.condition)
my_electric_car.drive_car()
print(my_electric_car.condition)
