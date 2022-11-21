# References:
# https://www.pythontutorial.net/python-basics/python-read-text-file/
# https://stackoverflow.com/questions/30282305/python-coding-error-file-doesnt-exist
# https://www.pythontutorial.net/python-basics/python-check-if-file-exists/
# https://www.programiz.com/python-programming/examples/read-line-by-line
# https://bobbyhadz.com/blog/python-split-elements-
# in-list#:~:text=To%20split%20the%20elements%20of,string%20you%20want%20to%20keep.
# https://www.w3schools.com/python/ref_func_round.asp

 
def process_scores_list():
    scores_list = []
    with open('scores.txt', 'r') as file_contents:
        for line in file_contents:
            try:
                score = line.strip().split(",")[1]
                scores_list.append(int(score))
            except:
                pass
    return scores_list
        
        
def display_list(scores_list):
    print('Scores:', scores_list)
    
    
def calculate_average(scores_list):
    total = sum(scores_list)
    average = round(total / (len(scores_list)), 2)
    return average
    
    
def calculate_max(scores_list):
    maximum = max(scores_list)
    return maximum


def calculate_min(scores_list):
    minimum = min(scores_list)
    return minimum


def display_stats(maximum, minimum, average):
    print("Your maximum score is: " + str(maximum))
    print("Your minimum score is: " + str(minimum))
    print("Your average score is: " + str(average))
   
   
def main():
    scores_list = process_scores_list()
    display_list(scores_list)
    maximum = calculate_max(scores_list)
    minimum = calculate_min(scores_list)
    average = calculate_average(scores_list)
    display_stats(maximum, minimum, average)
    
    
main()
