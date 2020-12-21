# Project - Tip Calculator
**Author:**     Jessica Cassidy\
**Date:**       October 4, 2020

## Description: 
This program prompts user for their food bill without tip, asks the user to choose between 3 tip options, then calculates sum of the food bill total and tip.
**Input:** Food Cost and Tip Option

**Output:** Food Total w/ Tip

## Pseudocode:
- Declare foodBill
- Declare tipPercentage
- Display "How much is your food bill (not including a tip)?"
- Input Float foodBill
- Display "How much would you like to add as a tip? Choose one of the following options: a. 20%  b. 15% c. 10%: Enter a lowercase character only: a, b, or c: "
- Input tipPercentage character a, b, or c
- Set, if statements for tip options a, b, c
    - if(tipPercentage == 'a'): print("Your bill total is: ", "{:.2f}".format(foodBill * a + foodBill))
    - if(tipPercentage == 'b'): print("Your bill total is: ", "{:.2f}".format(foodBill * b + foodBill))
    - if(tipPercentage == 'c'): print("Your bill total is: ", "{:.2f}".format(foodBill * c + foodBill))
- Display "Your bill total is: ", "{:.2f}".format(foodBill * tipPercentage + foodBill)

## Sample Program:
How much is your food bill (not including a tip)? ___\
How much would you like to add as a tip?\
Choose one of the following options: a. 20%  b. 15% c. 10%:\
Enter a lowercase character only: a, b, or c: ___\
Your bill total is: $ 0.00

## Program Output Example:
How much is your food bill (not including a tip)? 50.63\
How much would you like to add as a tip?\
Choose one of the following options: a. 20%  b. 15% c. 10%:\
Enter a lowercase character only: a, b, or c: a\
Your bill total is: $ 60.76
