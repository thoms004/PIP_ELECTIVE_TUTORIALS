"""
Simple ROI (Return on Investment) Calculator

ROI is calculated using the formula:
    ROI (%) = ((current_value - investment_amount) / investment_amount) * 100

Inputs:
    - current_value: The current value of the investment or revenue.
    - investment_amount: The initial amount invested.
Output:
    - ROI in percentage format.
"""

current_value = float(input("Enter the current value: "))
investment_amount = float(input("Enter the investment amount: "))

if investment_amount == 0:
    print("Investment amount cannot be zero.")
else:
    roi = ((current_value - investment_amount) / investment_amount) * 100

    print(f"Return on Investment (ROI): {roi:.2f}%")
