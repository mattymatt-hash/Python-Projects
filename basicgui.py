import tkinter

"""
* Name         : program name basic gui
* Author       : Matthew Stevens
* Created      : Creation Date 6-26
* Course       : CIS189
* IDE          : Visual Studio Code
* Description  : The purpose of this program is to create a simple GUI. The input is making the selection. the output is the text in the window once a selection has been made.
*
* Academic Honesty: I attest that this is my original work.
* I have not used unauthorized source code, either modified or
* unmodified.
"""
# Define functions for each Checkbutton's trigger
def pick_breakfast():
    """Update label to show 'Breakfast!' wen  Breakfast checkbutton is selected."""
    label.config(text="Breakfast!")

def pick_second_breakfast():
    """Update label to show 'Second Breakfast!' wen checkbutton is selected."""
    label.config(text="Second Breakfast!")

def pick_lunch():
    """Update label to show 'Lunch!' wen checkbutton is selected."""
    label.config(text="Lunch!")

def pick_dinner():
    """Update label to show 'Dinner!' wen checkbutton is selected."""
    label.config(text="Dinner!")

# Create main window
m = tkinter.Tk()
m.title("Favorite Meal")

# Create a label with text "Waiting"
label = tkinter.Label(m, text="Waiting")
label.grid(row=5)

# Add Checkbuttons with event triggers
var1 = tkinter.IntVar()
tkinter.Checkbutton(m, text="Breakfast", variable=var1, command=pick_breakfast).grid(row=1)

var2 = tkinter.IntVar()
tkinter.Checkbutton(m, text="Second Breakfast", variable=var2, command=pick_second_breakfast).grid(row=2)

var3 = tkinter.IntVar()
tkinter.Checkbutton(m, text="Lunch", variable=var3, command=pick_lunch).grid(row=3)

var4 = tkinter.IntVar()
tkinter.Checkbutton(m, text="Dinner", variable=var4, command=pick_dinner).grid(row=4)

# Add Exit button
exit_button = tkinter.Button(m, text="Exit", width=25, command=m.destroy)
exit_button.grid(row=6)

# Start main event loop
m.mainloop()
