"""
* Name         : input_while_exit.py
* Author       : Matthew Stevens
* Created      : 6-10-2025
* Course       : CIS189
* IDE          : Visual Studio Code
* original Description  : The purpose of this program is it prompts for numeric 
input between 1 and 100 (including endpoints). If the user provides a number outside of 1-100,
 the function prompts the user until a number within the valid range is provided.  the input is 
 what the user enters and the out put is the printed value along with the number of the users attempts
*
*new description same as old except with the exit loop a user can type a q for quit and immediately stop running the program.
*
* Academic Honesty: I attest that this is my original work.
* I have not used unauthorized source code, either modified or
* unmodified.
*
*to do this new objective the input will be read as a string first instead of an int to check for input that
*is not an actual number
*
"""

def get_valid_number():
    tries = 0
    while True:
        user_input = input("Enter number between 1 and 100 or 'q' to quit: ")
        if user_input.lower() == 'q':
            print("User quits.")
            break
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
# Input  "-1"  "101" "6" "q"
# output loops back to the start and asks you to enter a number between 1 and 100 , 
# loops back to the start and asks you to enter a number between 1 and 100, specified value = 5, number of tries = 3,
# user quits



