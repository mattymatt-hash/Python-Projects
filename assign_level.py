"""
* Name         : program name Selection using Dictionary Assignment
* Author       : Matthew Stevens
* Created      : Creation Date 6-22
* Course       : CIS189
* IDE          : Visual Studio Code
* Description  : The purpose of this program is to implement a switch case... The input is the levels... The output is the number of ponts for each level
*
* Academic Honesty: I attest that this is my original work.
* I have not used unauthorized source code, either modified or
* unmodified.
"""

def switch_level(level):
    """
    Return points for your level
    and points associated with the level.
    or 0 if the level is not recognized.
    """
    level_points = {
        'N': 50,    # Novice
        'B': 150,   # Beginner
        'E': 300,   # Experienced
        'A': 500    # Advanced
    }

    return level_points.get(level, 0)


def main:
    levels = ['N', 'B', 'E', 'A']

    for lvl in levels:
        points = switch_level(lvl)
        print(f"Level '{lvl}' earned you {points} points.")


if __name__ == "__main__":
    main()