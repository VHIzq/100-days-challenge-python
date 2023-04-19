#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇

print('Trip for Us')

bill = input('What was the total bill?')
tip = input('Whar percentage tip would you like yo give? 10, 12 or 15?')
persons = input('How many people to split the bill')

bill_float = float(bill)
tip_int = int(tip)
persons_int = int(persons)

tip_per_person = (bill_float / persons_int) * (tip_int / 100)

bill_per_person = (bill_float / persons_int) + tip_per_person

value_round = '{:.2f}'.format(bill_per_person)

message = f'Each person should pay {value_round}'

print(message)