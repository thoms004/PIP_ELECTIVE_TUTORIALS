"""
Calculation of square root of a number using Newton-Raphson Method

The Newton-Raphson method is an iterative numerical technique to find the root of a real-valued function.
For finding the square root of a number (N), we solve the equation f(x) = x^2 - N = 0.

Steps of the method:
1. Start with an initial guess (x), which can be the number itself.
2. Use the formula:
   x_next = (x + N / x) / 2
   This formula comes from applying the Newton-Raphson iteration to the function f(x).
3. Repeat the iteration until the value converges to a desired precision or for a fixed number of iterations.
4. The final value of x will be the square root of the number.

This program implements the method with 10 fixed iterations and displays the result.
"""

# Input: Accept a number from the user
number = float(input("Enter a number: "))

# Check if the input is negative
if number < 0:
    print("Cannot calculate square root of negative numbers")
else:
    # Initialize the guess as the input number
    x = number

    # Perform 10 iterations of the Newton-Raphson method
    for _ in range(10):
        x = (x + number / x) / 2

    # Output the result with 3 decimal places
    print(f"Square root of {number} is approximately {x:.3f}")
