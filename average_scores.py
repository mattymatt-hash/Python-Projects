"""
* Name         : average_scores.py
* Author       : Matthew Stevens
* Created      : 5/31/2025
* Course       : CIS189
* IDE          : Visual Studio Code
* Description  : The purpose of this program is to find a users average grade. The inputs are name first and last, age, 3 scores and the output when u take the total scores divided by the amount of scores will give you your average.
*
* Academic Honesty: I attest that this is my original work.
* I have not used unauthorized source code, either modified or
* unmodified.
"""
first_name = input("Enter first name: ")
last_name = input("Enter last name: ")
age = int(input("Enter age: "))

NUM_SCORE = 3

score1 = float(input("Enter 1-100: "))
score2 = float(input("Enter 1-100: "))
score3 = float(input("Enter 1-100: "))

average_grade = (score1 + score2 + score3) / NUM_SCORE

print(f"{last_name}, {first_name} age: {age} average grade: {average_grade:.2f}")