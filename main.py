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

#Imports all the required functions from my other files: for the main func:
from display import display_menu, display_password, display_saved_passwords, display_generation_config, display_single_password
from generator import generate_password
from analyser import analyse_password
from storage import load_passwords, delete_password, add_password, label_exists

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
        lower = input("Do you want to include lower characters in your password (y/n)? ")
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

def main():
    #Infinite loop:
    while True:
        #Displays the main menu:
        display_menu()
        #Validates the user's choice (the one he makes at the main menu):
        try:
            user_choice = int(input("Please choose an option (1-5)"))
        except ValueError:
            print("Please choose a numerical option (1-5)")
            continue
        if user_choice not in range(1,6):
            print("That option is not supported. Please choose an option between 1 and 5")
            continue
        #If user wants to generate a password:
        if user_choice == 1:
            #Calls all the funcs:
            display_generation_config()
            length, use_lower, use_upper, use_digits, use_symbols = get_generation_config()
            password = generate_password(length, use_lower, use_upper, use_digits, use_symbols)
            analysis = analyse_password(password)
            display_password(password, analysis)
            #Asks the user if he wants to save:
            answer = input("Do you want to save this password (y/n)? ")
            if answer.lower() in ["y", "yes"]:
                label = input("Please input the password's label:")
                passwords = load_passwords()
                #If the label already exists:
                if label_exists(passwords, label) == True:
                    print("This label already exists. Please choose a new one: ")
                    continue
                #If label is empty:
                if label.strip() == "":
                    print("Please1 input a label and not an empty space:")
                #Saves if the user chose yes and the label is valid:
                strength = analysis["rating"]
                add_password(passwords, label, password, strength)
                continue
        #If user wants to view the saved passwords:
        if user_choice == 2:
            passwords = load_passwords()
            display_saved_passwords(passwords)
        #If user wants to delete a password:
        if user_choice == 3:
            passwords = load_passwords()
            if not passwords:
                print("There are no passwords saved yet.")
                continue
            #Displays saved passwords so that the user sees the index:
            display_saved_passwords(passwords)
            #Ask + Validates index to delete:
            try:
                index = int(input("Please input the password's index:"))
            except ValueError:
                print("Please choose an allowed numerical value: ")
                continue
            if index > len(passwords) or index < 1:
                print("Please choose a correct numerical value:")
                continue
            index -= 1
            #Asks the user to confirm:
            prompt = input("Are you sure you want to delete this password ?")
            if prompt.lower() not in ["yes", "y"]:
                continue
            #Deletes the password if the index is valid
            delete_password(passwords, index)
        #If user wants to view a specific password based on index:
        if user_choice == 4:
            passwords = load_passwords()
            if not passwords:
                print("There are no passwords saved yet.")
                continue
            #Ask user for index + validates it:
            try:
                entry = int(input("Please input the password's index:"))
            except ValueError:
                print("Please choose a numerical value: ")
                continue
            if entry > len(passwords) or entry < 1:
                print("Please choose a correct numerical value:")
                continue
            entry -= 1
            entry = passwords[entry]
            #Displays the password if the entry was correct:
            display_single_password(entry)
        #If user wants to quit the program:
        if user_choice == 5:
            print("Thanks for using the Python Password Generator, see you next time :) !")
            break

#If statement that helps run the main function:
if __name__ == "__main__":
    main()
