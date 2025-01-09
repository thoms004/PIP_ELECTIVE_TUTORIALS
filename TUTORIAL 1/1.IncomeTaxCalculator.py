"""
Logic
~ Up to ₹2,50,000: No tax
~ ₹2,50,001 to ₹5,00,000: 5%
~ ₹5,00,001 to ₹10,00,000: 20%
~ Above ₹10,00,000: 30%
"""

income = int(input("Enter your Income:"))
if income <= 250000:
    tax = 0
    print("0% Tax")
elif income > 250000 and income <= 500000:
    tax = income * 0.05
    print("5% Tax\n" + "Tax Amount:", tax)
elif income > 500000 and income <= 1000000:
    tax = income * 0.2
    print("20% Tax\n" + "Tax Amount:", tax)
elif income > 1000000:
    tax = income * 0.3
    print("30% Tax\n" + "Tax Amount:", tax)