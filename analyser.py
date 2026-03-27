""" Sees strength scores as you test generation. The analyser is completely self-contained — it receives a password string and returns results, knowing nothing about how the password was made.

-Functions to write:
_______________________________________________________________________________________________________________________________________________________________________________________________
1) calculate_score(password) — takes a password string, applies the scoring criteria and returns a numeric score from 0 to 100. 
Awards points for length milestones, awards points for each character category detected as present in the password, applies penalties for weak compositions. 
This function contains all the mathematical logic.
_______________________________________________________________________________________________________________________________________________________________________________________________
2) get_strength_rating(points) — takes the numeric score and returns the corresponding rating string and emoji.
A simple series of comparisons mapping score ranges to labels. Keeps the rating logic separate from the scoring logic.
_______________________________________________________________________________________________________________________________________________________________________________________________
3) get_visual_bar(points) — takes the numeric score and returns a formatted string showing the visual progress bar of filled and empty blocks plus the percentage. 
Purely cosmetic, purely string manipulation.
_______________________________________________________________________________________________________________________________________________________________________________________________
4) analyse_password(password) — the public-facing function that the rest of the project calls. 
Calls the three functions above in sequence and returns a dictionary containing the score, rating and visual bar all together. 
This means the rest of the project only needs to call one function from this file rather than three.
_______________________________________________________________________________________________________________________________________________________________________________________________
"""

#Imports string module to be used in calculate_score funct:
import string

#Function that calculates the passwords strength score/points (0-100) based on length and character category, and penalizes passwords with only one category. 
def calculate_score(password):
    #Empty variable to store the points:
    points = 0
    #Variable that defines the passwords length:
    length = len(password)
    #Accords points based on the passwords length:
    if length < 8:
        return "password is not valid"
    if 8 <= length <= 11:
        points += 15
    if 12 < length <= 15:
        points += 25
    if 16 < length <= 19:
        points += 35
    if 20 < length <= 24:
        points += 45
    if length >= 25:
        points += 60
    #Checks for character types in the password calculates the points accordingly:
    if any(ch in string.ascii_lowercase for ch in password):
        points += 10
    if any(ch in string.ascii_uppercase for ch in password):
        points += 10
    if any(ch in string.digits for ch in password):
        points += 10
    if any(ch in string.punctuation for ch  in password):
        points += 10
    #Counts how many character categories are present in the password:
    categories_count = sum([
    any(ch in string.ascii_lowercase for ch in password),
    any(ch in string.ascii_uppercase for ch in password),
    any(ch in string.digits for ch in password),
    any(ch in string.punctuation for ch in password)
])
    #Takes off 20 points if only 1 category is present in the password:
    if categories_count == 1:
        points -= 20
    #Instores a cap at 100 points (not necessary but still):
    if points > 100:
        points = 100
    #Returns the number of points
    return points

#Function that takes the points given by calculate_score and converts them in a string that displays the strength and a bar that visually represents it:
def get_strength_rating(points):
    #Creates a variable to store the result:
    result = ""
    #Checks the passwords rating:
    if points <= 39:
        result += "Faible ❌"
    elif points<= 59:
        result += "Moyen ⚠️"
    elif points <= 79:
        result += "Fort ✅"
    elif points <= 99:
        result += "Très fort 💪"
    else:
        result += "Excellent 🙌"
    #Returns the result:
    return result

#Function that takes the points given by the calculate_score func and coverts it to a progress bar with a percentage score next to it:
def get_visual_bar(points):
    #Calculates how many filled blocks there need to be:
    filled_blocks = points // 10 
    #Calculates how many empty blocks there need to be:
    empty_blocks = 10 - filled_blocks
    #Puts the filled and empty blocks next to the total percentage out of 100:
    bar = f"[{filled_blocks * '█'}{empty_blocks * '░'}] {points}%"
    #Returns the result
    return bar

#Grouping function that combines the functions above and formats correctly the results:
def analyse_password(password):
    #Defines points:
    points = calculate_score(password)
    #Converts the function's results to a dictionary:
    difficulty = {
        "score" : points,
        "strength" : get_strength_rating(points),
        "bar" : get_visual_bar(points)
    }
    #returns the dictionary:
    return difficulty