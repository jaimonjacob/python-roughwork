def greet_user(first, last, middle = ''):
  '''Takes the first and last name and returns a fill name'''
  if middle:
    full_name = f'{first} {middle} {last}'
  else:  
    full_name = f'{first} {last}'
  return full_name

print(greet_user('John', 'Doe', 'Henry'))

