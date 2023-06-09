#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

length_letter = len(letters)
length_symbols = len(symbols)
length_number = len(numbers)

letter_str = ''
number_str = ''
symbol_str = ''

# Eazy Level - Order not randomised:
# e.g. 4 letter, 2 symbol, 2 number = JduE&!91

for char in range(1, (nr_letters + 1)):
  number_letter = random.randint(1, (length_letter - 1))
  random_letter = letters[number_letter]
  letter_str += random_letter

for char in range(1, (nr_numbers + 1)):
  number_number = random.randint(1, (length_number - 1))
  random_number = numbers[number_number]
  number_str += random_number

for char in range(1, (nr_symbols + 1)):
  symbol_str += random.choice(symbols)
  
password = letter_str + number_str + symbol_str

print(f'Here is your password: {password}')
# Hard Level - Order of characters randomised:
# e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

random_password = ''
string_list = list(password)
random.shuffle(string_list)

for char in string_list:
  random_password += char
print(f'Here is your Fort Knox password: {random_password}')
