# Program: Check Integer Range
# Description: Checks if an integer value is within or outside of range.

# Input: None
# Output:
# __  is within the range.
# __ is outside the range.

# Program Output Example:
# 5  is within the range.
# 4  is outside the range.
# 1  is within the range.

# Pseudocode:
# Module Main()
  # Call checkRange(5, 1, 10)
  # Call checkRange(5, 1, 10)
  # Call checkRange(5, 1, 10)
# End Main

# Module checkRange
  # If value < lower or value > upper Then
    # Display value, " is outside the range."
  # Else Then
    # Display value, " is within the range."
# End checkRange

# Call Main()

def main():
  checkRange(5, 1, 10)
  checkRange(4, 5, 10)
  checkRange(1, 1, 1)

def checkRange(value, lower, upper):
  if value < lower or value > upper:
    print(value, " is outside the range.")
  else:
    print(value, " is within the range.")

main()