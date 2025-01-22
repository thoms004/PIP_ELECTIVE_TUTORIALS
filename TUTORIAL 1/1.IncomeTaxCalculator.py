"""
Logic

Up to 3,00,000	        Nil
3,00,001 to 7,00,000	5%
7,00,001 to 10,00,000	10%
10,00,001 to 12,00,000	15%
12,00,001 to 15,00,000	20%
Above 15,00,000	        30%
"""

annual_income = input("Enter the Annual Income: ")
annual_income = int(annual_income)

if annual_income <= 300000:
    print("no tax")
    percentage = '0%'

elif annual_income >= 300001 and annual_income <= 700000:
    annual_income = annual_income + annual_income * 0.05
    percentage = '5%'

elif annual_income>= 700001  and annual_income <= 1000000:
    annual_income = annual_income +  annual_income * 0.1
    percentage= '10%'

elif annual_income>= 1000001  and annual_income <= 1200000:
    annual_income = annual_income + annual_income * 0.15
    percentage = '15%'

elif annual_income>= 1200001  and annual_income <= 1500000:
    annual_income = annual_income +  annual_income * 0.2
    percentage= '20%'

elif annual_income>= 1500001:
    annual_income = annual_income +  annual_income * 0.3
    percentage= '30%'
 
print("The calculated Income tax is", annual_income,"and the percentage is", percentage)