# References:
# https://www.pythontutorial.net/python-basics/python-read-text-file/
# https://stackoverflow.com/questions/30282305/python-coding-error-file-doesnt-exist
# https://www.pythontutorial.net/python-basics/python-check-if-file-exists/
# https://www.programiz.com/python-programming/examples/read-line-by-line
# https://bobbyhadz.com/blog/python-split-elements-
# in-list#:~:text=To%20split%20the%20elements%20of,string%20you%20want%20to%20keep.

def verify_file():
    import os.path
    file_exists = os.path.exists('/Users/jessharkness/Desktop/CIS 106/scores.txt')
    
    
def process_scores_list():
    scores_list = []
    with open('/Users/jessharkness/Desktop/CIS 106/scores.txt','r') as file_contents:
        file_contents = file_contents.readlines()
        file_contents = [new_line.strip() for new_line in file_contents]
        file_contents.remove('Name,Score')
        for lines in file_contents:
            test_scores = file_contents[0].split(',')
            scores_list.append(test_scores[1])
            scores_list = [int(i) for i in scores_list]
    return scores_list
        
        
def display_list(scores_list):
    print(scores_list)
    
    
def calculate_average(scores_list):
    total = sum(scores_list)
    average = total / (len(scores_list))
    return average
    
    
def calculate_max(scores_list):
    maximum = max(scores_list)
    return maximum


def calculate_min(scores_list):
    minimum = min(scores_list)
    return minimum

def display_stats(average, maximum, minimum):
    print("Your maximum score is: " + str(maximum))
    print("Your minimum score is: " + str(minimum))
    print("Your average score is: " + str(average))
   
   
def main():
    verify_file()
    scores_list = process_scores_list()
    display_list(scores_list)
    maximum = calculate_max(scores_list)
    minimum = calculate_min(scores_list)
    average = calculate_average(scores_list)
    display_stats(minimum, maximum, average)
    
    
main()


