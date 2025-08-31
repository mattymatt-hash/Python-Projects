"""
* Name         : program name CIS189 Module 7 File I/O Assignment.
* Author       : Matthew Stevens
* Created      : Creation Date 6-17
* Course       : CIS189
* IDE          : Visual Studio Code
* Description  : The purpose of this program is... The input is... The output is...
*
* Academic Honesty: I attest that this is my original work.
* I have not used unauthorized source code, either modified or
* unmodified.
"""

"""
CIS189 Module 7 File I/O Assignment.
"""

# ------------------------------------------------------------------------------
# Part 1.: Complete write_to_file function (void).
# ------------------------------------------------------------------------------

def write_to_file(scores, name="some-student-name"):
     """
     Parameters
     ----------
     scores: list
         List of scores.
     name: str
         Student name.
     """
     ##### YOUR CODE HERE #####

filename = f"{name}.txt"
    with open(filename, 'w') as file:
        for score in scores:
            file.write(f"{score}\n")



# ------------------------------------------------------------------------------
# Part 2: Complete get_student_info function (void).
# ------------------------------------------------------------------------------
     
def get_student_info():
    """
   inputs  student name and # of test scores  takes the scores and adds them into a list then outputs them as a file
    """
    # Create empty list to hold scores.
    ##### YOUR CODE HERE ######
 scores = []
    # Prompt for student name.
    ##### YOUR CODE HERE ######
student_name = input("Enter student name: ")
    # Prompt for number of scores to enter.
    nbr_scores = int(input("How many scores do you wish to enter? "))

    # Iterate up to nbr_scores, prompting user to enter a score each time.
    for i in range(nbr_scores):

        # Prompt for score.
        ##### YOUR CODE HERE #####
score = int(input(f"Enter the score your adding #{i + 1}: "))
        # Append score to scores list initialized above.
        ##### YOUR CODE HERE #####
scores.append(score)
    # Pass student scores and name to write_to_file function.
    ##### YOUR CODE HERE #####
write_to_file(score, name=student_name)


# ------------------------------------------------------------------------------
# Part 3: Complete read_from_file function (fruitful).
# ------------------------------------------------------------------------------

def read_from_file(filename):
    """
    Load scores from filename and return string containing filename,
    min score, max score and average score.

    Parameters
    ----------
    filename: str
        Name of file with scores, assumed to have .txt extension.

    Returns
    -------
    str
        String containing filename, min score, max score and average score.
    """
    # Open filename for reading. Load scores into list performing necessary
    # type conversions.
    ##### YOUR CODE HERE #####
with open(filename, 'r') as file:
        scores = [int(line.strip()) for line in file]
    # Identify min, max and average score from list of scores.
    ##### YOUR CODE HERE #####
 min_score = min(score)
    max_score = max(score)
    avg_score = sum(score) / len(score)
    # Return string formatted as {filename}: min={min_score}, max={max_score} avg={avg_score}
    ##### YOUR CODE HERE #####
 return f"{filename}: min={min_score}, max={max_score}, avg={avg_score:.2f}"
    # Replace pass with your return string.
    "matt.txt: min=50, max=100, avg=75"



if __name__ == "__main___":

    # Call get_student_info for 3 students.
    ##### YOUR CODE HERE #####
get_student_info()
get_student_info()
get_student_info()
    # Call read_from_file for created text files and print the results.
    ##### YOUR CODE HERE #####
print(read_from_file("user1.txt"))
    print(read_from_file("user2.txt"))
    print(read_from_file("user3.txt"))
    # Remove pass upon completion.
    pass
