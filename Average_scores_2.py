"""
* Name : average_scores2.py
* Author : Matthew Stevens
* Created : 6/7/2025
* Course : CIS189
* IDE : Visual Studio Code
* Description : The purpose of this program is to find a users average grade. The
inputs are name first and last, age, 3 scores and the output when u take the total
scores divided by the amount of scores will give you your average.
*
* Academic Honesty: I attest that this is my original work.
* I have not used unauthorized source code, either modified or
* unmodified.
"""
# get first name
try:
    first_name = input("Enter first name: ")
    print(f"First name: {first_name}")                # could include validation so numbers arent entered for first and last names
except Exception as e:
    print(f"try again: {e}")  # if error print error message
    first_name = "Unknown"  # default name

try:
    last_name = input("Enter last name: ")
    print(f"last name:{last_name}")
except Exception as e:
    print(f"try again: {e}")
    last_name = "Unknown"

try:
    age_input = input("Enter age: ")  # get age
    age = int(age_input) # convert to integer
    if age <= 0:  # check age
     raise ValueError (f"try again") # raise VE if age is wrong
except ValueError:
    print("Invalid age input. Setting age to 0.")
except Exception as ee:
    print(f"wrong: {ee}") # wrong age message
    age = 0  # default to zero

NUM_SCORE = 3 # total scores to be entered

try:
    score1 = float(input("Enter score 1 (1-100): "))         # ------------------
    score2 = float(input("Enter score 2 (1-100): "))         # enter your grades
    score3 = float(input("Enter score 3 (1-100): "))        #--------------------
    average_grade = (score1 + score2 + score3) / NUM_SCORE
except ValueError:
    print("wrong, start over.")  # message for wrong number
    score1 = score2 = score3 = 0.0  # revert scores back to 0
    average_grade = 0.0   # assign all average grades 0
except Exception as eee:
    print(f"try again: {eee}")  # any other errors
    score1 = score2 = score3 = 0.0 #revert scores to zero
    average_grade = 0.0    #all grades 0

print(f"{last_name}, {first_name} | Age: {age} | Average Grade: {average_grade:.2f}")

