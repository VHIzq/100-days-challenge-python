#Write your code below this line 👇

def prime_checker(number):
  is_div_by_one = number % 1 == 0
  is_div_by_self = number % number == 0
  print(is_div_by_one)
  print(is_div_by_self)

#Write your code above this line 👆
    
#Do NOT change any of the code below👇
n = int(input("Check this number: "))
prime_checker(number=n)

""" 
Prime numbers are numbers that can only be cleanly divided by themselves and 1.
It's a prime number.
It's not a prime number.
"""