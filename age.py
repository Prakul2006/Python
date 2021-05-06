#!/bin/python3

pyear = 2020
print ('ADVANCED AGE CALCULATOR')
print ('- By Prakul K Hebbur')
print('\n')

print ('Caluclate your age below ')
print('\n')

year = input('For which year should I caluclate your age for ? (Eg :- 2020 , 1945 ,2050)')
print('\n')
year = int(year)
if year > 1:
    if year > pyear:
      born = input('What year were you born ? (Eg :- 2006, 1945, 2001)')
      print('\n')
      born = int(born)
      age = (year - born)
      if year >= born:
          print('You\'ll be',age,'years old in year',year)
      else:
        print('ERROR ' * 3)
        print('STOP Joking ! How can you born in future')
    elif year < pyear:
      born = input('What year were you born ? (Eg :- 2006, 1945, 2001)')
      print('\n')
      born = int(born)
      age = (year - born)
      page = (pyear - born)
      if year >= born:
          print('You\'re',age,'years old in',year,'.''You grew so fast ! Now you\'r age is',page,'years.')
      else:
        print('ERROR ' * 3)
        print('STOP Joking ! Please check the values you have entered !')
    elif year == pyear:
      born = input('What year were you born ? (Eg :- 2006, 1945, 2001)')
      print('\n')
      born = int(born)
      age = (year - born)
      if year >= born:
          print('You\'re',age,'years old now. Congratulations ! Have a Great life ahead !')
      else:
        print('ERROR ' * 3)
        print('STOP Joking ! Please check the values you have entered !')
else:
    print('ERROR ' * 3)
    print('I can only caluclate age in AD')
