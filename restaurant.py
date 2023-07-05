class Restaurant:
  """A simple restaurant class."""

  def __init__(self, restaurant_name, cuisine_type):
    """Initialize restaurant name and cuisine type arguments."""
    self.restaurant_name = restaurant_name
    self.cuisine_type = cuisine_type

  def describe_restaurant(self):
    """Describes a restaurant."""
    print(f"The restaurant is called {self.restaurant_name}.")
    print(f"The cuisine type is {self.cuisine_type}.")

  def open_restaurant(self):
    """Describes that restaurant is open."""
    print(f"The restaurant {self.restaurant_name} is open.")


class Icecreamstand(Restaurant):

  def __init__(self, restaurant_name, cuisine_type, flavours):
    super().__init__(restaurant_name, cuisine_type)
    self.flavors = flavours

  def describe_flavors(self):
    for value in self.flavors:
      print(f'This restaurant has {value}')

store_1 = Icecreamstand('store 1', 'icecream',
                        ['vanila', 'chocolate', 'cranberry'])

store_1.describe_flavors()