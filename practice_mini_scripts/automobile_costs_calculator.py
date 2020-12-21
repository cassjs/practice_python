# Program: Automobile Costs Calculator
# Description: Program prompts user for various automobile expenses and adds them together
# showing monthly and annual totals.

# Input:
# Enter your monthly expense for loan payments:
# Enter your monthly expense for insurance:
# Enter your monthly expense for gas:
# Enter your monthly expense for oil:
# Enter your monthly expense for tires:
# Enter your monthly expense for maintenance:

# Output:
# Your monthly automobile expenses total is $0.00
# Your annual automobile expenses total is $0.00

# Program Output Example:
# Enter your monthly expense for loan payments: 168.40
# Enter your monthly expense for insurance: 83.20
# Enter your monthly expense for gas: 80
# Enter your monthly expense for oil: 10
# Enter your monthly expense for tires: 5
# Enter your monthly expense for maintenance: 50
# Your monthly automobile expenses total is $396.60.
# Your annual automobile expenses total is $4759.20.

def main():
  loan = float()
  insurance = float()
  gas = float()
  oil = float()
  tires = float()
  maintenance = float()
  loan, insurance, gas, oil, tires, maintenance = getExpenses()
  showExpenses(loan, insurance, gas, oil, tires, maintenance)

def getExpenses():
  loan = float(input('Enter your monthly expense for loan payments: '))
  insurance = float(input('Enter your monthly expense for insurance: '))
  gas = float(input('Enter your monthly expense for gas: '))
  oil = float(input('Enter your monthly expense for oil: '))
  tires = float(input('Enter your monthly expense for tires: '))
  maintenance = float(input('Enter your monthly expense for maintenance: '))
  return loan, insurance, gas, oil, tires, maintenance

def showExpenses(loan, insurance, gas, oil, tires, maintenance):
  totalMonthly = loan + insurance + gas + oil + tires + maintenance
  totalAnnual = totalMonthly * 12
  print('Your monthly automobile expenses total is $', "{:.2f}".format(totalMonthly), '.', sep='')
  print('Your annual automobile expenses total is $', "{:.2f}".format(totalAnnual), '.', sep='')

main()