#Write your code below this line 👇

def prime_checker(number):
  is_prime = True
  for div in range(2, number):
    if number % div == 0:
      is_prime = False
  if is_prime:
    print("It's a prime number.")
  else:
    print("It's not a prime number.")
      
    
#Write your code above this line 👆
    
#Do NOT change any of the code below👇
n = int(input("Check this number: "))
prime_checker(number=n)

""" 
Prime numbers are numbers that can only be cleanly divided by themselves and 1.
It's a prime number.
It's not a prime number.
"""