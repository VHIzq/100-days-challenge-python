# 🚨 Don't change the code below 👇
year = int(input("Which year do you want to check? "))
# 🚨 Don't change the code above 👆

# Write your code below this line 👇

""" 
this is how you work out whether if a particular year is a leap year.

on every year that is evenly divisible by 4 

**except** every year that is evenly divisible by 100 

**unless** the year is also evenly divisible by 400
"""

is_divisible_by_4 = year % 4 == 0
print(is_divisible_by_4)

is_divisible_by_100 = year % 100 == 0
print(is_divisible_by_100)

is_divisible_by_400 = year % 400 == 0
print(is_divisible_by_400)


if is_divisible_by_4:
    if is_divisible_by_100:
        if is_divisible_by_400:
            print('Leap year.')
        else:
            print('Not leap year.')

    else:
        print('Leap year.')

else:
    print('Not leap year.')
