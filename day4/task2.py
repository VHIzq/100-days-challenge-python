import random

# Import the random module here

# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

names_length = len(names)

random_number = random.randint(0, names_length - 1)

selected_guest = names[random_number]

message = f'{selected_guest} is going to buy the meal today!'
print(message)