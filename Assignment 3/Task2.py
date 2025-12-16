"""Problem Statement: Write a Python program that:
1.   Asks the user for a number as input.
2.   Uses the math module to calculate the:
o   Square root of the number
o   Natural logarithm (log base e) of the number
o   Sine of the number (in radians)
3.   Displays the calculated results.
"""

import math

num = int(input("Enter the Number: "))

print(f"Square root of the Number: {math.sqrt(num)}")
print(f"Logartihm: {math.log(num)}")
print(f"Sine: {math.sin(num)}")