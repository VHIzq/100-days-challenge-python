print('Welcome to the rollercoaster!')
heght = int(input('Whats your height in cm?'))

if heght >= 120:
  print('You can ride the rollercoster')
  
  age = int(input('Whats your age?'))
  if age < 12:
    print('Please pay 5 dlls')
  elif age <= 18:
    print('Please pay 7 dlls')
  else:
    print('Please pay 12 dlls')

else:
  print('Sorry, you must grow taller before you can ride')