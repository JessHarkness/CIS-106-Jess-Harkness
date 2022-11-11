# This program takes a line of text and
# displays it backwards.
# References:
# https://thispointer.com/remove-duplicate-spaces-from-string-in-python/
# https://www.digitalocean.com/community/tutorials/python-remove-spaces-from-string


def get_text():
    print("Enter a line of text.")
    user_text = str(input())
    return user_text


def process_string(user_text):
    user_text = user_text.strip()
    user_text = " ".join(user_text.split())
    backwards_text = user_text[::-1]
    return backwards_text


def display_string(backwards_text):
    print(str(backwards_text))
    
    
def main():
    user_text = get_text()
    backwards_text = process_string(user_text)
    display_string(backwards_text)
   
   
main()
