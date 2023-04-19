# 🚨 Don't change the code below 👇
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
height_float = float(height)
height_square = height_float ** 2
bmi = round(float(weight) / float(height_square))

""" 
Under 18.5 they are underweight
Over 18.5 but below 25 they have a normal weight
Over 25 but below 30 they are slightly overweight
Over 30 but below 35 they are obese
Above 35 they are clinically obese.
"""

underweight = bmi < 18.5
normal_weight = bmi < 25
slightly_overweight = bmi < 30
obese = bmi < 30
clinically_obese = bmi < 35

if underweight:
  print(f'Your BMI is {bmi}, you are slightly underweight.')
elif normal_weight:
  print(f'Your BMI is {bmi}, you have a normal weight')
elif slightly_overweight:
  print(f'Your BMI is {bmi}, you are slightly overweight')
elif obese:
  print(f'Your BMI is {bmi}, you are obese')
elif clinically_obese:
  print(f'Your BMI is {bmi}, you are clinically obese.')
else:
  print('Introduce your real height and weight')
