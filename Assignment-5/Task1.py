
'''Problem Statement: Write a Python program that:
1.   Creates a dictionary where student names are keys and their marks are values.
2.   Asks the user to input a student's name.
3.   Retrieves and displays the corresponding marks.
4.   If the student’s name is not found, display an appropriate message.
'''
students = {
    'Alice': '85',
    'John': '95',
    'Carol': '75',
}

name = input("Enter the Student's name: ")

if name in students:
    print(f"{name}'s marks: {students[name]}") 
else:
    print("Student not found")