"""
-Functions to write:
_____________________________________________________________________________________________________________________________________________________________________________________________________________________
1) display_menu() — prints the main menu with the ASCII border and all five options.
_____________________________________________________________________________________________________________________________________________________________________________________________________________________
2) display_password(password, analysis) — prints a generated password clearly with its strength bar, rating and score beneath it. Receives the password string and the analysis dictionary from analyse_password().
_____________________________________________________________________________________________________________________________________________________________________________________________________________________
3) display_saved_passwords(passwords) — prints all saved passwords as a numbered list showing index, label, date saved, strength rating and the password itself. Handles the empty list case with a friendly message.
_____________________________________________________________________________________________________________________________________________________________________________________________________________________
4) display_single_password(entry) — prints the full details of one specific saved password entry when the user selects option 4. Shows all fields clearly formatted.
_____________________________________________________________________________________________________________________________________________________________________________________________________________________
5) display_generation_config() — prints the configuration prompts header before the user enters their generation preferences. Just a visual separator to make the config section feel distinct from the menu.
_____________________________________________________________________________________________________________________________________________________________________________________________________________________
"""

#Function that prints the main menu:
def display_menu():
    print("+---------------------------------------------------------------------+")
    print("|                          PASSWORD GENERATOR                         |")
    print("+---------------------------------------------------------------------+")
    print("|     1) Generate a password                                          |")
    print("|     2) View a saved password                                        |")
    print("|     3) save a password (with a label)                               |")
    print("|     4) View a (specific according to label) saved password          |")        
    print("|     5) Delete a saved password                                      |")
    print("+---------------------------------------------------------------------+")

#Function that displays the password and underneath it its strength string, bar and percentage:
def display_password(password,analysis):
    #Checks if password exists:
    if not password:
        print("There is no password to display")
        return
    #Checks if analysis exists
    if not analysis:
        print("There is no analysis of the password yet")
        return
    #If analysis and password exists prints them:
    print("")
    print(f"{password}")
    print(f"{analysis['bar']}")
    print(f"{analysis['score']}")
    print(f"{analysis['rating']}")
    print("")

#Function that prints all existing passwords along with their index, label, date saved and strength rating:
def display_saved_passwords(passwords):
    #Checks if there are any saved passwords:
    if not passwords:
        print("There are no passwords saved yet. Please save one to be able to access this function.")
        return 
    #Prints the password along with the pertaining information:
    for index, item in enumerate(passwords, start = 1):
        print(f"{index} {item['label']}, {item['date']}, {item['rating']}, {item['password']}")

#Function that prints the whole details of a single password:
def display_single_password(entry):
    #Checks if the entry exists:
    if not entry:
        print("This password hasn't been saved yet.")
        return
    #Prints all the password's information:
    print(f"{entry['label']}")
    print(f"{entry['date']}") 
    print(f"{entry['rating']}")
    print(f"{entry['password']}")