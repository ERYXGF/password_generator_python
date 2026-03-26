"""
________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________
-Functions to write:
________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________
1) get_generation_config() — handles all user input for configuring a new password. Asks for length with validation, asks for each category toggle with validation, checks that at least one category is selected, 
and returns the configuration as a set of values ready to pass to generate_password(). This is a helper that keeps the main loop clean.
________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________
2) main() — the main loop. Initialises nothing except the while True loop. Calls display_menu(), gets the user's choice with try/except, dispatches to the right logic for each option. 
Option 1 calls get_generation_config() then generate_password() then analyse_password() then display_password() then asks if they want to save. Option 2 loads and displays saved passwords. 
Option 3 handles deletion with confirmation. Option 4 handles single password display. Option 5 breaks the loop with a goodbye message.
________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________
3) The if __name__ == "__main__" guard at the bottom calls main().
________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________
"""

#Helper function for the generate_password func in generator.py:
def get_generation_config():
    #Asks user for password length: checks if the length is a number:
    while True:
        try:
            length = int(input("Please choose the password's wanted length (8-128): "))
        except ValueError:
            print("The length should be a number between 8 and 128")
            continue
        #Checks if the length is amidst the allowed min and max values:
        if length < 8 or length > 128:
            print("The password's length is not between the allowed values (8-128). Please try again: ")
            continue
        break
    #Determines which character categories the user wants to include:
    while True:
        use_lower = False
        use_upper = False
        use_digits = False
        use_symbols = False
        lower = input("Do you wan to include lower characters in your password (y/n)? ")
        if lower.lower() in ["yes", "y"]:
            use_lower = True
        upper = input("Do you want to include upper characters in your password (y/n)? ")
        if upper.lower() in ["yes", "y"]:
            use_upper = True
        digits = input("Do you want to include digits in your password (y/n)? ")
        if digits.lower() in ["yes", "y"]:
            use_digits = True
        symbols = input("Do you want to include symbols/punctuation in your password (y/n)? ")
        if symbols.lower() in ["yes", "y"]:
            use_symbols = True
        #Checks if at least one category is selected:
        if use_lower == False and use_upper == False and use_digits == False and use_symbols == False:
            print("No character category was selected. Please select one to be able to generate a password: ")
            continue
        break
    #Returns the length and wanted character categories:
    return length, use_lower, use_upper, use_digits, use_symbols