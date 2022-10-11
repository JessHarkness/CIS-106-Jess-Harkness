def displayResult(multiplier, i, solutions):
    print(str(multiplier) + " * " + str(i) + " = " + str(solutions))

def processExpressions(multiplier, numberOfExpressions):
    for i in range(1, numberOfExpressions + 1, 1):
        solutions = i * multiplier
        displayResult(multiplier, i, solutions)
        
    return solutions

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
