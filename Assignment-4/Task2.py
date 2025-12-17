'''
Problem Statement: Write a Python program that:
1.   Takes user input and writes it to a file named output.txt.
2.   Appends additional data to the same file.
3.   Reads and displays the final content of the file.

'''
from pathlib import Path
file = Path("sample.txt")
text = input("Enter the Text to Write to the file: ")
text2= input("Enter additional text to append: ")

with open(file,'a') as f:
    f.write(text+"\n")
    f.write(text2)
    print("Data successfully appended.")
    
with open(file,'r') as f:
    print("Final content of sample.txt : ")
    lines = f.readlines()
    for line in lines:
        print(line.rstrip('\n'))