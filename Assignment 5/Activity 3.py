def calculateKilometers(miles):
    kilometers = miles * 1.609344
    
    return kilometers

def calculateMeters(kilometers):
    meters = kilometers * 1000
    
    return meters

def displayResult(miles, kilometers, meters, centimeters):
    print(str(miles) + " miles is: " + str(kilometers) + 
          " kilometers, " + str(meters) + " meters, " + 
          str(centimeters) + " centimeters. ", end='', flush=True)

def calculateCentimeters(meters):
    centimeters = meters * 100
    
    return centimeters

def getMiles():
    print("Enter your distance in miles:")
    miles = float(input())
    
    return miles

# Main
# This program takes an input distance in miles and converts it to kilometers, meters, and centimeters.
# References: https://www.mathisfun.com/measure/us-standard-length.html
# References: https://www.testingdocs.com/user-defined-functions-in-flowgorithm/
miles = getMiles()
kilometers = calculateKilometers(miles)
meters = calculateMeters(kilometers)
centimeters = calculateCentimeters(meters)
displayResult(miles, kilometers, meters, centimeters)
