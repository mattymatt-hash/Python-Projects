"""
* Name         : program name Function Keyword & Arbitrary Arguments
* Author       : Matthew Stevens
* Created      : Creation Date 6-15
* Course       : CIS189
* IDE          : Visual Studio Code
* Description  : The purpose of this program is to calculaye an average score from a list of vlues The input is a list of variable numbers and students info The output is the students info and the users average score
*
* Academic Honesty: I attest that this is my original work.
* I have not used unauthorized source code, either modified or
* unmodified.
"""
def average_score(*scores, **student_info):
    if len(scores) == 0:
        average = 0
    else:
        average = sum(scores) / len(scores)

    name = student_info.get("name", "Unknown")
    gpa = student_info.get("gpa", "N/A")
    course = student_info.get("course", "N/A")

    return f"Result: name = {name} gpa = {gpa} course = {course} with current average {average:.1f}"


def main():
    result1 = average_score(90, 80, 70, name="Alice", gpa=3.5, course="Biology")
    print(result1)

    result2 = average_score(88, name="Bob", gpa=2.9, course="History")
    print(result2)

    result3 = average_score(60, 75, 85, 90, 95, name="Charlie", gpa=3.8, course="Computer Science")
    print(result3)


if __name__ == "__main__":
    main()

'''
Result: name = Alice gpa = 3.5 course = Biology with current average 80.0
Result: name = Bob gpa = 2.9 course = History with current average 88.0
Result: name = Charlie gpa = 3.8 course = Computer Science with current average 81.0
'''