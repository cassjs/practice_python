# Program: Cubed Integer
# Description: Program prompts user for an integer to be cubed and shows the cubed result.
# User is also prompted to continue program.

# Input:
# Enter a value to be cubed.

# Output:
# ___ cubed is ___
# Enter another value to be cubed?
# Enter Yes to continue.

# Program Output Example:
# Enter a value to be cubed. 4
# 4 cubed is 64
# Enter another value to be cubed?
# Enter Yes to continue. Yes
# Enter a value to be cubed. 2
# 2 cubed is 8
# Enter another value to be cubed?
# Enter Yes to continue. yes
# Enter a value to be cubed. 10
# 10 cubed is 1000
# Enter another value to be cubed?
# Enter Yes to continue.

# Pseudocode:
# Set finished = False
# Set value as an Integer
# Set cube as an Integer
#
# while(not finished):
    # Set value as an Integer
    # Input value 'Enter a value to be cubed. '
    # Set cube = value * value * value
    # Display value, 'cubed is', cube
    #
    # Display 'Enter another value to be cubed?'
    # Set String keepLooping
    # Input keepLooping 'Enter Yes to continue. '
    #
    # If keepLooping == 'yes' or 'Yes':
        # Set finished = False
    # Else:
        # Set finished = True

finished = False
value = int()
cube = int()
while (not finished):
    value = int(input('Enter a value to be cubed. '))
    cube = (value * value * value)
    print(value, 'cubed is', cube)

    print('Enter another value to be cubed?')
    keepLooping = str(input('Enter Yes to continue. '))

    if keepLooping == 'yes' or 'Yes':
        finished = False
    else:
        finished = True