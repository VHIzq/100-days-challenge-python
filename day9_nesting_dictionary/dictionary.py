programming_dictionary = {
  "Bug": "An error in a program that prevents the program from running as expected.",
  "Function": "A piece of code that you can easily call over and over again."
  }

#print(programming_dictionary['Bug'])

""" new entry """
programming_dictionary['Function'] = 'new def'

""" create an empty dic """
empty_dictionary = {}

""" wipe a dic """
#programming_dictionary = {}
#print(programming_dictionary)

""" edit an item in a dic """
programming_dictionary["New Bug"] = 'A moth in ur laptop'

#print(programming_dictionary)


""" loop through a dic """
for item in programming_dictionary:
  print(item)
  print(programming_dictionary[item])