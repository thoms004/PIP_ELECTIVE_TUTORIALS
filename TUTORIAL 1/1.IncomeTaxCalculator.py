"""
Logic
~ Up to ₹2,50,000: No tax
~ ₹2,50,001 to ₹5,00,000: 5%
~ ₹5,00,001 to ₹10,00,000: 20%
~ Above ₹10,00,000: 30%
"""

annual_income = input("Enter the annual Income ")
annual_income = int(annual_income)

if annual_income <= 250000:
    print("no tax")

elif annual_income >= 250000 and annual_income <= 500000:
    annual_income = annual_income + annual_income * 0.05
    percentage = '5%'

elif annual_income>= 500000  and annual_income <= 1000000:
    annual_income = annual_income +  annual_income * 0.05
    percentage('20')

elif annual_income >= 1000000:
    annual_income = annual_income + annual_income * .20
    percentage = '30%'
 
print("The calculated Income tax is", annual_income,"and the percentage is", percentage)
