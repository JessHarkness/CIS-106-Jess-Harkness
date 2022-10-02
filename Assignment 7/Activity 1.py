def calculateGrossPay(hours, payRate):
    if hours > 40:
        overtimeRate = 1.5
        overtime = (hours - 40) * overtimeRate * payRate
        grossPay = 40 * payRate + overtime
    else:
        grossPay = hours * payRate
    
    return grossPay

def displayResult(grossPay):
    print("You earned: " + str(grossPay) + " dollars this week. ")

def getHours():
    print("Enter the number of hours you worked this week: ")
    hours = float(input())
    
    return hours

def getPayRate():
    print("Enter your pay rate per hour: ")
    payRate = float(input())
    
    return payRate

# Main
# This program asks a user for their hours
# worked, and pay rate per hour, to
# calculate their gross pay over one week.
# References: https://www.weisbergcummings.com/weighted-overtime-pay#%20/#:~:text=Overtime%20refers%20to%20the%20time,above%2040%20hours%20per%20week.
hours = getHours()
payRate = getPayRate()
grossPay = calculateGrossPay(hours, payRate)
displayResult(grossPay)
