# Exercise 1
class User:

  def __init__(self, first_name, last_name, age, team):
    self.first_name = first_name
    self.last_name = last_name
    self.age = age
    self.team = team
    self.login_attempts = 0

  def describe_user(self):
    print(
      f'\nUser First Name: {self.first_name}\nUser Last Name: {self.last_name} \nUser Age: {self.age} \nUser Team: {self.team}'
    )

  def greet_user(self):
    '''Describes a user'''
    print(f'Hellow {self.first_name}')

  def increment_login_attmepts(self):
    '''Increments login attempts'''
    self.login_attempts += 1
    print(f'Current login attempts are {self.login_attempts}')

  def reset_login_attmepts(self):
    '''Resets login attempts'''
    self.login_attempts = 0
    print(f'Current login attempts are {self.login_attempts}')


class Privilages:
  
  def __init__(self, privilages):
    self.privilages = privilages

  def show_privilages(self):
    for value in self.privilages:
      print(f'{value}')


class Admin(User):

  def __init__(self, first_name, last_name, age, team, privilages):
    super().__init__(first_name, last_name, age, team)
    self.privilages = Privilages(privilages)


