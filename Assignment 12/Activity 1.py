# This program takes grade scores from a user
# and displays the average, minimum, and maximum.

# Reference: 
# https://www.askpython.com/python/array/python-add-elements-to-an-array
# References: https://www.w3schools.com/python/ref_list_append.asp


def display_instructions():
    print("Input a negative number when you are done entering scores.")


def get_score():
    print("Enter a score:")
    score = float(input())
    return score


def get_scores_list():
    list_of_scores = []
    while True:
        score = get_score()
        if not (score >= 0):
            break
        list_of_scores.append(score)
    
    return list_of_scores


def calculate_average(list_of_scores):
    total = sum(list_of_scores)
    average = total / (len(list_of_scores))
    return average


def calculate_minimum(list_of_scores):
    minimum = min(list_of_scores)
    return minimum
    
    
def calculate_maximum(list_of_scores):
    maximum = max(list_of_scores)
    return maximum


def display_score_stats(average, minimum, maximum):
    print("Your maximum score is: " + str(maximum))
    print("Your minimum score is: " + str(minimum))
    print("Your average score is: " + str(average))


def main():
    display_instructions()
    list_of_scores = get_scores_list()  

    average = calculate_average(list_of_scores)
    minimum = calculate_minimum(list_of_scores)
    maximum = calculate_maximum(list_of_scores)

    display_score_stats(average, minimum, maximum)
    

main()
