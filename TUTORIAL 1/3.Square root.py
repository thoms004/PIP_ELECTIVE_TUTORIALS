"""
Calculation of square root of a number using Newton Raphson Method

"""
number= float(input("Enter a number:"))

if number < 0:
  print("Cannot Calculate square root of a negative number.")
else:
  x = number
  for i in range(10) :
    x=(x+number/x)/2
  print(f"Square root of {number} is {x:.3f}")
