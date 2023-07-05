class Car:
  """A simple attempt to represent a car."""

  def __init__(self, make, model, year):
    self.make = make
    self.model = model
    self.year = year
    self.odometer_reading = 0

  def get_descriptive_name(self):
    long_name = f"{self.year} {self.make} {self.model}"
    return long_name.title()

  def read_odometer(self):
    print(f"This car has {self.odometer_readin} miles on it.")

  def update_odometer(self, mileage):
    if mileage >= self.odometer_reading:
      self.odometer_reading = mileage
    else:
      print("You can't roll back the odometer!")

  def increment_odometer(self, miles):
    self.odometer_reading + miles

  def fill_gastank(self):
    print('the tank is full')


class Battery:
  '''initiating a simple battery class'''

  def __init__(self, battery_size=50):
    self.battery_size = battery_size

  def describe_battery(self):
    """Print a statement describing the battery size."""
    print(f"This car has a {self.battery_size}-kWh battery.")

  def get_range(self):
    if self.battery_size == 50:
      range = 250
    elif self.battery_size == 100:
      range = 500
    print(f'This car can go upto {range} on full charge')

  def upgrade_battery(self):
    if (self.battery_size != 100):
      self.battery_size = 100
    print(f'Battery size is now upgraded to {self.battery_size}')


class ElectricCar(Car):
  '''Initialize attributes of the parent class. Then initialize attributes specific to an electric car.'''

  def __init__(self, make, model, year):
    """Initialize attributes of the parent class."""
    super().__init__(make, model, year)
    self.battery = Battery()

  def fill_gastank(self):
    print('this tank doesnt need a battery')
