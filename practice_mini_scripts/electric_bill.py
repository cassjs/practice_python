# Program: Electric Bill

# Description: Input the amount of electricity use in kilowatt-hours and the cost per a kilowatt-hour, 
# then calculate the total monthly electric bill after including an 8% sales tax. 

# Input: 
# Enter the amount of electricity used in kilowatt-hours (kWh) used in one month:
# What is the cost of electricity per kilowatt-hour?
# Program Output Example: 
# Enter the amount of electricity used in kilowatt-hours (kWh) used in one month:
# 908
# What is the cost of electricity per kilowatt-hour?
# .12
# Total bill w/out sales tax: $108.96
# Sales Tax Applied = 8%
# Total sales tax: $8.72
# Total bill w/ sales tax: $117.68

# Pseudocode:
# Declare Real amountUsed
# Input Real amountUsed 'Enter the amount of electricity used\nin kilowatt-hours (kWh) used in one month: '

# Declare Real costPerHr
# Input Real costPerHr 'What is the cost of electricity per kilowatt-hour? '

# Set totalBeforeTax = amountUsed * costPerHr
# Display 'Total bill w/out sales tax: ' $0.00

# Declare taxAmount = .08
# Display 'Sales Tax Applied = 8%'
# Set totalSalesTax = totalBeforeTax * taxAmount
# Display 'Total sales tax: ' $0.00 

# Set totalAfterTax = totalBeforeTax + totalSalesTax
# Display 'Total bill w/ sales tax: ' $0.00

amountUsed = float(input('Enter the amount of electricity used\nin kilowatt-hours (kWh) used in one month:\n'))

costPerHr = float(input('\nWhat is the cost of electricity per kilowatt-hour?\n'))

totalBeforeTax = amountUsed * costPerHr
print("\nTotal bill w/out sales tax: $", "{:.2f}".format(totalBeforeTax), sep='')

taxAmount = .08
print('\nSales Tax Applied = 8%')
totalSalesTax = totalBeforeTax * taxAmount
print("Total sales tax: $", "{:.2f}".format(totalSalesTax), sep='')

totalAfterTax = totalBeforeTax + totalSalesTax
print("\nTotal bill w/ sales tax: $", "{:.2f}".format(totalAfterTax), sep='')