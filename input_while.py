"""
* Name         : input_while.py
* Author       : Matthew Stevens
* Created      : 6-9-2025
* Course       : CIS189
* IDE          : Visual Studio Code
* Description  : The purpose of this program is it prompts for numeric 
input between 1 and 100 (including endpoints). If the user provides a number outside of 1-100,
 the function prompts the user until a number within the valid range is provided.  the input is 
 what the user enters and the out put is the printed value along with the number of the users attempts
*
* Academic Honesty: I attest that this is my original work.
* I have not used unauthorized source code, either modified or
* unmodified.
"""

def get_valid_number():
    tries = 0
    while True:
        tries += 1
        try:
            value = int(input("Enter number between 1 and 100: "))
            if 1 <= value <= 100:
                print(f"specified value = {value}, number of tries = {tries}")
                break
            else:
                print("wrong. Try again.")
        except ValueError:
            print("Wrong. enter a number.")

if __name__ == "__main__":
    get_valid_number()

# test
# Input    "whatsup" 300 "-21" -100 "5"
# output wrong enter a number , wrong try again,wrong try again,wrong try again, specified value = 5, number of tries = 5

# test
# Input 69
# Output 69 number of tries = 1
