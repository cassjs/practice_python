# Program: Reverse Integer using Modulus and Floor Division
# Description: Prompts user to enter a two-digit number, then reverses the two-digit integer the user entered.

# Input:
# Enter a two-digit integer:

# Output:
# __'s digit: __
# __'s digit: __
# __

# Program Output Example:
# Enter a two-digit integer: 23
# 1's digit: 3
# 10's digit: 2
# 32

# Pseudocode:
# Input Integer num 'Enter a two-digit integer:'
# Set onesDigit = num % 10
# Set tensDigit = num // 10
#
# Display "1's digit:", onesDigit
# Display "10's digit:", tensDigit
#
# Input num(onesDigit * 10 + tensDigit)




num = int(input('Enter a two-digit integer: '))
onesDigit = num % 10
tensDigit = num // 10

print("1's digit:", onesDigit)
print("10's digit:", tensDigit)

num = input(onesDigit * 10 + tensDigit)