""" Positional Args """

def greet_with(name, location):
  print(f'Hello {name}')
  print(f'What is it like in {location}')

#greet_with('Raven', 'Titans Tower')

""" Keywords Args """
def greet_with_keywords(location, name):
  print(f'Hello {name}')
  print(f'What is it like in {location}')

greet_with_keywords(name='Raven', location='Titans Tower')



