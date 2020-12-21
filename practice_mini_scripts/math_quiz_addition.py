# Program: Math Quiz (Addition)
# Description: Program randomly produces a sum of two integers. User can input the answer
# and recieve a congrats message or an incorrect message with the correct answer.

# Input:
# Random Integer + Random Integer = ____
# Enter your answer:

# Output:
# Correct = Congratulations!
# Incorrect = The correct answer is ____

# Program Output Example:
# Correct
  # 22 + 46 = ___
  # Enter your answer: 68
  # Congratulations!
# Incorrect
  # 75 + 16 = ___
  # Enter your answer: 2
  # The correct answer is 91.

# Pseudocode:
# Main Module
  # from numpy import random
  # Set num1 = random.randint(100)
  # Set num2 = random.randint(100)
  # Display num1, '+', num2, '= ___ '
  # Set correctAnswer = num1 + num2
  # Set userAnswer = getUserAnswer()
  # Call checkAnswer(userAnswer, correctAnswer)
# End Main

# Module getUserAnswer():
  # Set userAnswer = int(input('Enter your answer: '))
  # Return userAnswer

# Module checkAnswer(userAnswer, correctAnswer):
  # If userAnswer == correctAnswer:
    # Display 'Congratulations!'
  # Else:
    # Display 'The correct answer is ', correctAnswer, '.', sep=''
# End checkAnswer

# Call Main

def main():
  from numpy import random
  num1 = random.randint(100)
  num2 = random.randint(100)
  print(num1, '+', num2, '= ___ ')
  correctAnswer = num1 + num2
  userAnswer = getUserAnswer()
  checkAnswer(userAnswer, correctAnswer)

def getUserAnswer():
  userAnswer = int(input('Enter your answer: '))
  return userAnswer

def checkAnswer(userAnswer, correctAnswer):
  if userAnswer == correctAnswer:
    print('Congratulations!')
  else:
    print('The correct answer is ', correctAnswer, '.', sep='')

main()