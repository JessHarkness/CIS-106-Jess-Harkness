def displayAverage(average):
    print("Your average score is: " + str(average))

def getScores():
    print("Enter a score:")
    score = float(input())
    
    return score

def instructions():
    print("Input any negative number when you are done entering scores.")

def processScores():
    sum = 0
    count = 0
    while True:    #This simulates a Do Loop
        score = getScores()
        sum = sum + score
        count = count + 1
        if not(score >= 0): break   #Exit loop
    sum = sum - score
    average = sum / (count - 1)
    displayAverage(average)

# Main
# This program calculates an average score based on user input.
# Reference: https://www.freecodecamp.org/news/python-do-while-loop-example/
# Reference:https://realpython.com/python-do-while/
instructions()
processScores()
