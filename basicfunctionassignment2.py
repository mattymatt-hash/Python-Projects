"""
* Name         : Basic Function Assignment-2
* Author       : Matthew Stevens
* Created      : Creation Date: 6-7-2025
* Course       : CIS189
* IDE          : Visual Studio Code
* Description  : The purpose of this program is to show a basic function in python The input is name, hours worked, and hourly pay rate The output is name, hours worked, and hourly pay rate and the value of total pay plus adds return statement 
*
* Academic Honesty: I attest that this is my original work.
* I have not used unauthorized source code, either modified or
* unmodified.
"""

"""Asks for name, hours worked, hourly pay rate, then prints and returns answers.
 hours_worked and hourly_pay_rate as parameters
 returns the calculated weekly pay.
 """

def weekly_pay(hours_worked, hourly_pay_rate): 
    return hours_worked * hourly_pay_rate
def hourly_employee_input():
   
    try:
        name = input("Enter employee name: ")
        if not name.strip():
            raise ValueError("Name cant be empty.")
    except Exception as e:
        print(f"Error with name input: {e}")
        name = "Unknown"

    try:
        hours_worked = int(input("Enter hours worked: "))
        if hours_worked < 0:
            raise ValueError("Hours worked cant be neg.")
    except ValueError as e:
        print(f"Invalid input for hours worked: {e}")
        hours_worked = 0
    except Exception as e:
        print(f"Unexpected error: {e}")
        hours_worked = 0

    try:
        hourly_rate = float(input("hourly pay rate: "))
        if hourly_rate < 0:
            raise ValueError("Hourly rate cant be neg.")
    except ValueError as e:
        print(f"Invalid input for hourly rate: {e}")
        hourly_rate = 0.0
    except Exception as e:
        print(f"Unexpected error: {e}")
        hourly_rate = 0.0

    weekly_total = weekly_pay(hours_worked, hourly_rate)

    print( f"Employee: {name}, Hours Worked: {hours_worked}, "
        f"Weekly Pay: ${weekly_total:.2f}")

    return {
        "name": name,
        "hours_worked": hours_worked,
        "hourly_rate": hourly_rate,
        "weekly_pay": weekly_total
}

employee_data = hourly_employee_input()
print(
    f"Total weekly Pay for {employee_data['name']}: "
    f"${employee_data['weekly_pay']:.2f}"
)
