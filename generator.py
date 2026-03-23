"""Contains exclusively the password generation logic. The function that builds a password character by character, guaranteeing at least one character from each selected category. 
This is the most algorithmically interesting file. It contains 2 functions: one that builds a character pool by defining what characters are allowed (in list) and a list of individual character pools 
and a function thatactually contains the logic to generate the password."""

#Import the string module to be used in the get_character_pool func:
import string

#Function that based on what the users (boolean value in parameters) wish returns a list on what type of characters to be used in the generate password func:
def get_character_pool(use_lower = False, use_upper = False, use_digits = False, use_symbols = False):
    #Creates an empty list and string to store result:
    selected_char_lst = []
    selected_char_str = ""
    #Assigns a variable to each password character type:
    #Note to self/anybody reading the code: These 4 lines are only for readability, i could just append the wanted string module in the if statements directly if i wanted to.
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    digits = string.digits
    symbols = string.punctuation
    #User chooses which type of character the password will use:
    if use_lower == True:
        selected_char_lst.append(lower)
        selected_char_str += lower
    if use_upper == True:
        selected_char_lst.append(upper)
        selected_char_str += upper
    if use_digits == True:
        selected_char_lst.append(digits)
        selected_char_str += digits
    if use_symbols == True:
        selected_char_lst.append(symbols)
        selected_char_str += symbols
    #Returns a list and string of the available characters to be used in the generation of the password:
    return selected_char_lst, selected_char_str

#Function that generates the password based on what character types the user wants (see func above):
def generate_password(length, use_lower, use_upper, use_digits, use_symbols):
    pass