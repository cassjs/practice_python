# Program: Integer Checker 
# Description: Program checks a range of numbers and determines if the range or number
# equals 6 as the number itself, or when added/subtracted.

# Input: None
# Output:
# Not a magic 6.
# Magic 6!

# Program Output Example:
# Not a magic 6.
# Magic 6!
# Magic 6!
# Magic 6!

# Pseudocode:
# Module Main
  # Call magicSix()

# Module magicSix (num1, num2)
  # If num1 == 6 or num2 == 6 or num1 + num2 == 6 or num1 - num2 == 6 or num2 - num1 == 6 Then
     # Display “Magic Six!”
  # Else Then
     # Display “Not a magic 6.”
# End Module

def main():
  magicSix(5, 5)
  magicSix(6, 5)
  magicSix(4, 2)
  magicSix(4, 10)

def magicSix(num1, num2):
  if num1 == 6 or num2 == 6 or num1 + num2 == 6 or num1 - num2 == 6 or num2 - num1 == 6:
    print("Magic 6!")
  else:
    print("Not a magic 6.")

main()