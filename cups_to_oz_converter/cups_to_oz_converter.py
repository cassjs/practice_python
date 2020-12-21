# Program:    Cups to Fluid Ounces Converter
# Author:     Jessica Cassidy
# Date:       October 11, 2020
# Description: This program converts measurements in cups to fluid ounces.
# (1 cup = 8 fluid ounces)
# Input:      Number of Cups
# Output:     Number of Fluid Ounces

# Program Output Example:
# This program converts measurements in cups to fluid ounces.
# For your reference the formula is: 1 cup = 8 fluid ounces.
# Enter the number of cups: 24
# That converts to 192.0 fluid ounces.

# Pseudocode:
# Main Module
    # Call showIntro()
    # Input Real Cups "Enter the number of cups: "
    # Call cupsToOunces(cups)
# End Main

# Module showIntro()
    # Display "This program converts measurements in cups to fluid ounces.\nFor your reference the formula is: 1 cup = 8 fluid ounces."
# End showIntro()

# Module cupsToOunces(cups)
    # Set ounces = 8
    # Set Ounces = Real Cups * Ounces
    # Display "That converts to", ounces, "fluid ounces."
# End cupsToOunces(cups)

# Call Main

def main():
    showIntro()
    cups = float(input("Enter the number of cups: "))
    cupsToOunces(cups)

def showIntro():
    print(
        "This program converts measurements in cups to fluid ounces.\nFor your reference the formula is: 1 cup = 8 fluid ounces.")

def cupsToOunces(cups):
    ounces = 8
    ounces = float(cups) * ounces
    print("That converts to", ounces, "fluid ounces.")

main()