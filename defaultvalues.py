"""
* Name         : program name Default values assignment
* Author       : Matthew Stevens
* Created      : Creation Date 6-14-2025
* Course       : CIS189
* IDE          : Visual Studio Code
* Description  : The purpose of this program is to validate a users test score making sure its in the correct raqnge or giving an error message ig it is not
*inputs are test name, test message, invalid message, invalid test score out put is the score or an error message
* Academic Honesty: I attest that this is my original work.
* I have not used unauthorized source code, either modified or
* unmodified.
"""

def score_input(test_name, test_score=-1, invalid_message='Invalid test score!'):
    try:
        # Try convert to float
        score = float(test_score)
        if 0 <= score <= 100:
            return f"{test_name}: {score}"
        else:
            return f"{test_name}: {invalid_message}"
    except ValueError:
        return f"{test_name}: ValueError encountered!"
    