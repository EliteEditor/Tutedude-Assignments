'''
1.   Creates a list of numbers from 1 to 10.
2.   Extracts the first five elements from the list.
3.   Reverses these extracted elements.
4.   Prints both the extracted list and the reversed list

'''


list = [1,2,3,4,5,6,7,8,9,10]
print(f"original list:",list)
Extracted_list = list[0:5]
print("Extracted List:", Extracted_list)
reversed_list = Extracted_list[::-1]
print("Reversed List:", reversed_list)