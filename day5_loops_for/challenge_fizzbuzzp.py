""" 
  Your program should print each number from 1 to 100 in turn.

When the number is divisible by 3 then instead of printing the number it should print "Fizz".

When the number is divisible by 5, then instead of printing the number it should print "Buzz".`

  And if the number is divisible by both 3 and 5 e.g. 15 then instead of the number it should print "FizzBuzz"
"""


for number in range(1, 101):
  is_by_three = number % 3 == 0
  is_by_five = number % 5 == 0
  
  if is_by_three and is_by_five:
      print('FizzBuzz')
  
  elif is_by_three:
    print('Fizz')
  
  elif is_by_five:
    print('Buzz')
  
  else:
    print(number)
