# Program:     Pounds(lbs) to Kilograms(kg) Converter
# Author:      Jessica Cassidy
# Date:        October 4, 2020
# Description: This program prompts user to enter a weight in pounds(lbs) and converts it to Kilograms(kg). 
# The user input to enter weight in pounds gets reprompted infinitely after each conversion to kilograms(kg).
# Input:       Weight in Pounds(lbs)
# Output:      Weight in Kilograms(kg)
#
# // SAMPLE PROGRAM:
# Hello, this calculator converts weight in pounds(lbs) to kilograms(kg).
# Enter weight in pounds(lbs):
# Weight in Kilograms(kg):
#
# // PSEUDOCODE:
# Declare Real currentWeightlbs as 0.00
# Declare Real kilosPerlb as 0.453592
# Display "Hello, this calculator converts weight in pounds(lbs) to kilograms(kg)."
# While True:
    # Input "Enter weight in pounds (lbs): "
    # Input float currentWeightlbs
    # Set convertKilos = currentWeightlbs * kilosPerlb
    # Display "Weight in Kilograms (kg): 0.00"

currentWeightlbs = 0.00
kilosPerlb = 0.453592

print("Hello, this calculator converts weight \nin pounds (lbs.) to kilograms (kg)\n")
while True:
  currentWeightlbs = float(input("Enter weight in pounds(lbs): "))

  convertKilos = currentWeightlbs * kilosPerlb
  print("Weight in Kilograms(kg): " + "{:.2f}".format(convertKilos)+ "\n")