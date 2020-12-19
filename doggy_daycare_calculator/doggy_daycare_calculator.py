# Program:      Doggy Daycare Calculator
# Author:       Jessica Cassidy
# Date:         12/05/2020

# Description:  The Doggy Daycare Calculator calculates
# the number of dogs and hours entered by a user. The hours correspond to
# the Hours Rate Type: hourly, half day, and full day rates.

# // HOURS RATE TYPE:
# Hourly Rate (Max 2 hours)
# $7.00/hr, each dog
# Half Day Rate (Over 2 hrs - up to 5 hours max)
# $20.00 first dog, additional dogs $15 each
# Full Day Rate (Over 5 Hours - Up to 11 Hours Max)
# $30 first dog, additional dogs $25 each

# Input:        Enter Number of Dogs(numDogs) and Enter Number of Hours (numHours)
# Output:       Calculated Rate in USD $0.00

# // PSEUDOCODE:

# Module Main()
    # Declare int numDogs
    # Input int numDogs 'Enter Number of Dogs: '
    # Declare Real numHours
    # Input Real numHours 'Enter Number of Hourss: '
    # Call calcRate(numHours, numDogs)
    # Call output(numHours, numDogs)
# End Module Main
#
# Module calcRate(numHours, numDogs)
    # If numHours <= 2
        # Declare Real hourlyRate = numHours * numDogs * 7
        # Return Real hourlyRate
    # Else If numHours >=1 and numHours <= 5
        # If numDogs > 1
        # Declare halfDayRate = (20 + (15 * numDogs) - 15)
        # Return ("$" + "{:.2f}".format(halfDayRate))
        # Else Return $20.00
    # Else If numHours >= 5.01 and numHours <= 11.00
        # If numDogs > 1
        # Declare fullDayRate = (30 + (25 * numDogs) - 25)
        # Return Real fullDayRate
        # Else Display '$30.00'
    # Else If numHours >= 11.01
        # Return 'Hours exceeded. 11 hours is the max daycare hours available. Try again.''
# End Module calcRate
#
# Module output(numHours, numDogs)
#    Declare rateResult = calcRate(numHours, numDogs)
#    Display rateResult
# End Module output
#
# Call Main()

def main():
    numDogs = 0
    numDogs = int(input('Enter Number of Dogs: '))
    numHours = 0.00
    numHours = float(input('Enter Number of Hours: '))
    calcRate(numDogs, numHours)
    output(numDogs, numHours)

def calcRate(numDogs, numHours):
    if (numHours <= 2):  # Hourly Rate
        hourlyRate = (numHours * numDogs * 7)
        return("$" + "{:.2f}".format(hourlyRate))
    elif (numHours >= 1 and numHours <= 5):  # Half Day Rate
        if (numDogs > 1):
            halfDayRate = (20 + (15 * numDogs) - 15)
            return("$" + "{:.2f}".format(halfDayRate))
        else:
            return("$" + "{:.2f}".format(20.00))
    elif (numHours >= 5.01 and numHours <= 11.00):  # Full Day Rate
        if (numDogs > 1):
            fullDayRate = (30 + (25 * numDogs) - 25)
            return("$" + "{:.2f}".format(fullDayRate))
        else:
            return("$" + "{:.2f}".format(30.00))
    elif (numHours >= 11.01):  # Hours Exceeded
        return('Hours exceeded. 11 hours is the max daycare hours available. Try again.')

def output(numDogs, numHours):
    rateResult = calcRate(numDogs, numHours)
    print(rateResult)

main()