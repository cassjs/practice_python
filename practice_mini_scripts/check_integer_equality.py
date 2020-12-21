# Program: Check Integer Equality
# Description: Program checks if integer values are equal to each other and which integer is greater.

# Input:   None
# Output:  Result of checkEquality

# Program Output Example:
# The values are equal.
# 5 is greater than 4.
# 4 is greater than -1.

# Pseudocode:
# Main Module
  # Call checkEquality(5, 5)
  # Call checkEquality(5, 4)
  # Call checkEquality(-1, 4)
# End Main

# Module check Equality
  # If num1 == num2 Then
    # Display "The values are equal."
  # Else If num1 > num2 Then
    # Display num1 "is greater than" num2.
  # Else If num2 > num1 Then
    # Display num2 "is greater than" num1.
# End check Equality

def main():
  checkEquality(5, 5)
  checkEquality(5, 4)
  checkEquality(-1, 4)

def checkEquality(num1, num2):
  if num1 == num2:
    print("The values are equal.")
  elif num1 > num2:
    print(num1, " is greater than ", num2, ".",sep="")
  elif (num2 > num1):
    print(num2, " is greater than ", num1, ".",sep="")

main()