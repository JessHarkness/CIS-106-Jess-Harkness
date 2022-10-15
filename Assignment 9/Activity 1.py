def displayResult(multiplier, i, solutions):
    print(str(multiplier) + " * " + str(i) + " = " + str(solutions))

def getMultiplier():
    print("What number will be your multiplier?")
    multiplier = int(input())
    
    return multiplier

def getNumberOfExpressions():
    print("How many expressions do you want to generate?")
    numberOfExpressions = int(input())
    
    return numberOfExpressions

def processExpressions(multiplier, numberOfExpressions):
    i = 1
    while i < numberOfExpressions + 1:
        solutions = multiplier * i
        displayResult(multiplier, i, solutions)
        i = i + 1
    
    return solutions

# Main
# This program generates a given number of multiplication expressions for a given value.
# References: https://www.youtube.com/watch?v=GzVXu2TOYi0
# References: https://www.w3schools.com/python/python_while_loops.asp
multiplier = getMultiplier()
numberOfExpressions = getNumberOfExpressions()
processExpressions(multiplier, numberOfExpressions)
