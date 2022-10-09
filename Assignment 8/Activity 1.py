def displayResult(multiplier, numberOfExpressions, i):
    print(str(multiplier) + " * " + str(i) + " = " + str(i * multiplier))

def processExpressions(multiplier, numberOfExpressions):
    print("For " + str(numberOfExpressions) + " multiples of " + str(multiplier) + ": ")
    for i in range(1, numberOfExpressions + 1, 1):
        displayResult(multiplier, numberOfExpressions, i)

def getMultiplier():
    print("What number will be your multiplier?")
    multiplier = int(input())
    
    return multiplier

def getNumberOfExpressions():
    print("How many expressions do you want to generate?")
    numberOfExpressions = int(input())
    
    return numberOfExpressions

# Main
# This program generates a given
# number of multiplication expressions
# for a given multiplier.
# References: https://www.youtube.com/watch?v=2CtTJzXrxfU
# References: https://www.w3schools.com/python/python_for_loops.asp
multiplier = getMultiplier()
numberOfExpressions = getNumberOfExpressions()
processExpressions(multiplier, numberOfExpressions)
