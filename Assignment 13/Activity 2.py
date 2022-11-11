# This program takes a line of text and
# displays it backwards.

def get_text():
    print("Enter a line of text.")
    text_string = str(input())
    
    return text_string

def display_string_backwards(text_string):
    print(text_string[::-1])
    
def main():
    text_string = get_text()
    display_string_backwards(text_string)
    
main()
    