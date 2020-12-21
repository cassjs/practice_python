# Program: Birth Year Calculator
# Description: This program calculates a user's birth year by prompting user for their name, age, and wheter or not they had a birthday this year yet.

# Input:
# What is your name?
# How old are you?
# Did you have your birthday this year yet? Enter yes or no.

# Output:
# Hello _____! You were born in _____!

# Program Output Example:
# What is your name? Jack
# How old are you? 14
# Did you have your birthday this year yet? Enter yes or no. yes

name = input('What is your name? ')
age = int(input('How old are you? '))
birthday = input('Did you have your birthday this year yet? Enter yes or no. ')
currentYear = 2020
birthdayOver = currentYear - age # if birthday passed
birthdayWaiting = currentYear - age - 1 #if no birthday yet this year

if(birthday == 'yes'):
  print('Hello ', name+'! ', 'You were born in ', birthdayOver,'!', sep="")
else:
  print('Hello ', name+'! ', 'You were born in ', birthdayWaiting,'!', sep="")