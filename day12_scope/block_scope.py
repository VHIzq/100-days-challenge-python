""" Python doesn't have Block Scope 
while, if, for don't create a block scope
"""

game_level = 3
enemies = ['Skeleton', 'Zombie', 'Alien']

def create_enemy():
  if game_level < 5:
    new_enemy = enemies[0]

print(new_enemy)