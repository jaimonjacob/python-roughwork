# 9.13
from random import randint
from pprint import pprint
from random import choice

class Dice:
  def __init__(self, sides=6):
    self.sides = sides

  def roll_dice(self):
    current_side = randint(1, self.sides)
    print(f'the current side is {current_side}')

# 9.14
source_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'a', 'b', 'c', 'd', 'e']
my_value = 9;
for value in range(0,len(source_list)):
  cur_value = choice(source_list)
  print(cur_value)
  if(cur_value == my_value):
    break
print(f'you have won. the current value is {cur_value}')
  


