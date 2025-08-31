"""
* Name         : Basic if-elif Statement
* Author       : Matthew Stevens
* Created      : 6-1-2025
* Course       : CIS189
* IDE          : Visual Studio Code
* Description  : The purpose of this program is to let users pick a membership and display the cost of the one they chose. The input is asking the user if they want to sign up the membership selection and which memebership package they would like. The output is the cost/level of the membership they chose
*
* Academic Honesty: I attest that this is my original work.
* I have not used unauthorized source code, either modified or
* unmodified.
"""
print("Will you sign up for our Programmers Toolkit Monthly Subscribtion Box")
response = input().strip().lower()

if response == "yes":
    print("choose your desired membership")
    print("Platinum, Gold, Silver, Bronze, or Free Trial")
    level = input("Select One: ").strip().lower()

    if level == "platinum":
        print("Platinum Membership: $75/monthly")
    elif level == "gold":
        print("Gold Membership: $65/monthly")
    elif level == "silver":
        print("Silver Membership: $55/monthly")
    elif level == "bronze":
        print("Bronze Membership: $45/monthly")
    elif level == "free trial":
        print("Free Trial Membership: $0/monthly")
    else:
        print("error. Please choose from the list.")
 
elif response == "no":
    print("Then leave, You don't buy, then go away.")

else:
    print("select 'yes' or 'no'.")
 
