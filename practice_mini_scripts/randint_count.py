# Program: Random Integer Count
# Description: Program outputs 5 random numbers ranging from integer values 1 - 10.

# Input: None
# Output: Displays five random numbers in the range of 1-10

# Program Output Example:
# 10
# 7
# 5
# 10
# 2

# Pseudocode:
# Module Main():
  # For count in range(0,5)
    # Set number = random.randint(1, 10)
    # Display number
# End Main
#
# Call Main()

import random

def main():
  for count in range(0, 5):
    number = random.randint(1, 10)
    print(number)
main()

