'''
Task 2: Create a Personalized Greeting
Problem Statement: Write a Python program that:
1.  Takes a user's first name and last name as input.
2.  Concatenates the first name and last name into a full name.
3.  Prints a personalized greeting message using the full name.
'''

first=input("Enter your First Name: ")
last=input("Enter your last Name: ")

full_name=" ".join([first,last])

print("Hello, ",full_name)
