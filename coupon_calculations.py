"""
* Name         : coupon_calculations.py
* Author       : Matthew Stevens
* Created      : 6-2-2025
* Course       : CIS189
* IDE          : Visual Studio Code
* Description  : The purpose of this program is take user input and out put a total with shipping. 
* The inputs are price, cash coupon, and discount coupon The output expected is the total cost...in a 
* real world application i would probably add strip()) to line 23 so that users could enter the price with
* or without the dollar sign.      
*
* Academic Honesty: I attest that this is my original work.
* I have not used unauthorized source code, either modified or
* unmodified.
"""
# Constants
TAX_RATE = 0.07
SHIPPING_1 = 5.95
SHIPPING_2 = 7.95
SHIPPING_3 = 11.95
FREE_SHIPPING_THRESHOLD = 60.00

# input
original_price = float(input("Enter the original purchase price: "))
cash_coupon = int(input("Enter the value of your cash-off coupon ($10 or $15): "))
percent_coupon = int(input("Enter the percent discount coupon (10, 15, or 20): "))

# 1 cash-off coupon
price_after_cash_coupon = original_price - cash_coupon

# 2 Apply percent discount
discount = price_after_cash_coupon * (percent_coupon / 100)
price_after_percent_coupon = price_after_cash_coupon - discount

# 3 Determine shipping cost (based on pre-tax amount of the constant listed above ^^^^^^)
if price_after_percent_coupon < 20:
    shipping = SHIPPING_1
elif price_after_percent_coupon < 40:
    shipping = SHIPPING_2
elif price_after_percent_coupon < 60:
    shipping = SHIPPING_3
else:
    shipping = 0.0

# 4 figure out tax on discounted price
tax = price_after_percent_coupon * TAX_RATE

# 5  total cost
total_before_tax = price_after_percent_coupon + shipping
final_total = total_before_tax + tax

# Round to 2 decimal places
final_total = round(final_total, 2)

# Output final total
print("The total price of your order is: $", final_total)
