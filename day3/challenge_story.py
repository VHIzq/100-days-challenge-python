print('''
  
       .  . '    .                                             
      '   .            . '            .                +           
              `                          '    . '
        .                         ,'`.                         .
   .                  .."    _.-;'    `.              .    
              _.-"`.##%"_.--" ,'        `.           "#"     ___,,od000
           ,'"-_ _.-.--"\   ,'            `-_       '%#%',,/////00000HH
         ,'     |_.'     )`/-     __..--""`-_`-._    J L/////00000HHHHM
 . +   ,'   _.-"        / /   _-""           `-._`-_/___\///0000HHHHMMM
     .'_.-""      '    :_/_.-'                 _,`-/__V__\0000HHHHHMMMM
 . _-""                         .        '   _,////\  |  /000HHHHHMMMMM
_-"   .       '  +  .              .        ,//////0\ | /00HHHHHHHMMMMM
       `                                   ,//////000\|/00HHHHHHHMMMMMM
.             '       .  ' .   .       '  ,//////00000|00HHHHHHHHMMMMMM
     .             .    .    '           ,//////000000|00HHHHHHHMMMMMMM
                  .  '      .       .   ,///////000000|0HHHHHHHHMMMMMMM
  '             '        .    '         ///////000000000HHHHHHHHMMMMMMM
                    +  .  . '    .     ,///////000000000HHHHHHHMMMMMMMM
     '      .              '   .       ///////000000000HHHHHHHHMMMMMMMM
   '                  . '              ///////000000000HHHHHHHHMMMMMMMM
                           .   '      ,///////000000000HHHHHHHHMMMMMMMM
       +         .        '   .    .  ////////000000000HHHHHHHHMMMMMMhs
      
''')

print("Welcome to Science Research Ventures")
print("Your mission to find planetary resources is coming.\n")

""" story one """
print('You arrived with your elite scientists team into an unexplored planet \n with the only one mission to find weird chemical elements for the advance of your society.\n')

choose_l1 = input(print('Your ship landed in Xoo planet, \n What are you doing? Down: Leave from your ship \n Up: Stay inside the ship')).lower()

choose_l2 = input(print('You saw an asteroid hitting your ship, but you and your team are alived\n Need coverage against Gamma burst and X rays: \n Down: Run to a near great wall \n Up: Activate your emergency lab. A satellite land and transform into it.')).lower()

choose_l3 =input(print('All the team coverages from damaged inside the lab and start to analyze the elements from ground\n Up: Discover new elements and decide to stay in Xoo for more time \n Down: Decide to call Earth for getting a new ship replacements')).lower()

choose_l4 = input(print('Discover organic resources and water. Decide to create a new civilization beside Earth. \n Enter the new name  for your Civilization')).lower()

print(choose_l1)

if choose_l1 == 'up':
    print('Game Over: An asteroid hit your ship and explote.')

if choose_l1 == 'down':
    choose_l2
    
if choose_l2 == 'down':
    print('Game Over: A worm monter leaves from the wall and eat you')

if choose_l2 == 'up':
    choose_l3

if choose_l3 == 'down':
    print('Game over: Earth send you a new rocket but fail above your lab and everyone dies')

if choose_l3 == 'up':
    choose_l4

print(choose_l4)