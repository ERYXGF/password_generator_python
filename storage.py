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
from datetime import date

#Imports the path module:
from pathlib import Path

#Define what the file's path is:
passwords_path = Path("passwords.json")

#Function that loads passwords.json and returns the list of saved passwords:
def load_passwords():
    #Checks if the file exists:
    if not passwords_path.exists() or passwords_path.stat().st_size == 0:
        return []
    #Loads the file (if it exists), and handles corrupted JSON:
    try:
        with passwords_path.open("r", encoding = "utf-8") as f:
            data = json.load(f)
        return data if isinstance(data, list) else []
    except json.JSONDecodeError:
        return []
    
#Function that saves/dumps the passwords to the json file:
def save_passwords(passwords):
    #Saves the passwords (If they already exist):
    with passwords_path.open("w", encoding = "utf-8") as f:
        json.dump(passwords, f, indent = 4)

#Function that adds a password:
def add_password(passwords, label, password, strength):
    entry = {
        "label": label,
        "password": password,
        "strength": strength,
        "date": date.today().isoformat()
    }
    passwords.append(entry)
    save_passwords(passwords)
    return passwords
    
#Function that deletes a password:
def delete_password(passwords, index):
    #Checks if the index does exist:
    if not isinstance(index, int):
        return passwords
    if index < 0 or index >= len(passwords):
        return passwords
    #Deletes the password:
    del passwords[index]
    #Saves the updated information:
    save_passwords(passwords)
    return passwords

#Function that checks if a label already exists:
def label_exists(passwords, label):
    return any(entry.get("label") == label for entry in passwords)
