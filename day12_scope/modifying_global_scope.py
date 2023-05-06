#Modifying Global Scope
""" Only declaring the variable as global inside the functio you can change tje outer variable. """

enemies = 1

def increse_enemies():
  print(f'enemies inside the function: {enemies}')
  return enemies + 1
  
enemies = increse_enemies()
print(f'enemies outside the function: {enemies}')