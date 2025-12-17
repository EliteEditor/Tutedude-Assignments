'''
Task 1: Perform Basic Mathematical Operations
Problem Statement: Write a Python program that does the following:
1.  Takes two numbers as input from the user.
2.  Performs the basic mathematical operations on these two numbers:
o	Addition
o	Subtraction
o	Multiplication
o	Division
3.  Displays the results of each operation on the screen.

'''

print("Enter the Numbers to perform Operations")
num1=int(input("Enter the First Number: "))
num2=int(input("Enter the Second Number: "))

Addition = num1 + num2
Subtraction = num1 - num2
Multiplication = num1 * num2
Division = num1 / num2

print(f"Addition: {Addition}")
print(f"Subtraction: {Subtraction}")
print(f"Multiplication: {Multiplication}")
print(f"Division: {Division}")
