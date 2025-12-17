'''
Problem Statement:  Write a Python program that:
1.   Opens and reads a text file named sample.txt.
2.   Prints its content line by line.
3.   Handles errors gracefully if the file does not exist.
'''
i=1
try:
    with open("sample.txt", 'r') as f:
       lines = f.readlines()
       for line in lines:
         print(f"line {i}:{line.rstrip('\n')}")
         i+=1
         
except FileNotFoundError as fe:
    print(f"Error:the file 'sample.txt' was not found.")
        
