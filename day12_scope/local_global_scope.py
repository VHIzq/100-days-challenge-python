""" enemies = 1

def increase_enemies():
  enemies = 2
  enemies += 1
  print(f'Enemies inside the function: {enemies}')

increase_enemies()

print(f'Enemies outside the function: {enemies}') """

""" Global scope """
player_health = 10

def game():
  def drink_potion():
    potion_strenth = 2
  drink_potion()

game()
