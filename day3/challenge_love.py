# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

# Write your code below this line 👇
name_lower1 = name1.lower()
name_lower2 = name2.lower()

count = 0

letter_t = name_lower1.count('t')
letter_r = name_lower1.count('r')
letter_u = name_lower1.count('u')
letter_e = name_lower1.count('e')

letter_t2 = name_lower2.count('t')
letter_r2 = name_lower2.count('r')
letter_u2 = name_lower2.count('u')
letter_e2 = name_lower2.count('e')

sum_true = letter_t + letter_t2 + letter_r + letter_r2 + \
    letter_u + letter_u2 + letter_e + letter_e2

letter_o = name_lower1.count('o')
letter_l = name_lower1.count('l')
letter_v = name_lower1.count('v')
letter_e = name_lower1.count('e')

letter_l2 = name_lower2.count('l')
letter_o2 = name_lower2.count('o')
letter_v2 = name_lower2.count('v')
letter_e2 = name_lower2.count('e')

sum_love = letter_o + letter_l + letter_v + letter_e + \
    letter_l2 + letter_o2 + letter_v2 + letter_e2

score = str(sum_true) + str(sum_love)

score_coke = score <= '10' or score >= '90'
score_together = score >= '40' and score <= '50'

if score_coke:
    print(f'Your score is {score}, you go together like coke and mentos.')

elif score_together:
    print(f'Your score is {score}, you are alright together.')

else:
    print(f'Your score is {score}.')
