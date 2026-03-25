"""This file contains all the functins to store and save the passwords in json files.

-Functions to write:
_______________________________________________________________________________________________________________________
1) load_passwords() — loads passwords.json and returns the list of saved password dictionaries. 
Returns an empty list if the file doesn't exist yet. Handles corrupted JSON gracefully with a try/except.
_______________________________________________________________________________________________________________________
2) save_passwords(passwords) — takes the full passwords list and writes it to passwords.json. 
Called after every add or delete operation.
_______________________________________________________________________________________________________________________
3) add_password(passwords, label, password, strength) — takes the current passwords list, builds a new entry dictionary 
with label, password, strength rating and today's date, appends it to the list and calls save_passwords. 
Returns the updated list.
_______________________________________________________________________________________________________________________
4) delete_password(passwords, index) — takes the list and an integer index, removes the entry at that position, 
calls save_passwords and returns the updated list.
_______________________________________________________________________________________________________________________
5) label_exists(passwords, label) — takes the list and a label string, returns True if any existing entry has the same 
label, False otherwise. Used for duplicate label validation in main.py before saving.
_______________________________________________________________________________________________________________________
"""

#Imports the json module to be able to load, save and access the passwords in the json files:
import json

#Imports the path module:
from pathlib import Path

#Define what the file's path is:
passwords_path = Path("passwords.json")

#Function that loads passwords.json and returns the list of saved passwords:
def load_passwords(password):
    #Checks if the file exists:
    if not passwords_path.exists() or passwords_path.stat().st_size == 0:
        return ("There are no passwords saved yet.")
    #Loads the file (if it exists):
    with passwords_path.open("r", encoding = "utf-8") as f:
        return json.load(f)