list2 = [10, 20, 30, [40, 50, [60, 80, 90], 100, 110, 120], [112, 114, 116], 221, 226, 336]

# 1. Access First-Level Elements
print(list2[0])
print(list2[1])
print(list2[2])
print(list2[3])
print(list2[4])
print(list2[5])
print(list2[6])
print(list2[7])

# 2. What is the output of list2[0] and list2[3]?
print(list2[0]) # 10
print(list2[3]) # [40, 50, [60, 80, 90], 100, 110, 120]

# 3. Extract the list [40, 50, [60, 80, 90], 100, 110, 120] using indexing.
print(list2[3])

# 4. Retrieve 60, 80, and 90 from the nested list using indexing.
print(list2[3][2])

# 5. What is the output of list2[4][1]?
print(list2[4][1])

# 6. Write a statement to access the element 336.
print(list2[-1])

# 7. The last element (336).
print(list2[-1])

# 8. The second-to-last sub-list ([112, 114, 116]).
print(list2[4])
						
# 9. Access 110 from the sub-list [40, 50, [60, 80, 90], 100, 110, 120].
print(list2[3][4])
			
# 10. Retrieve the element 116 from the list [112, 114, 116].
print(list2[4][2])
	
# 11. Extract 40 from [40, 50, [60, 80, 90], 100, 110, 120].
print(list2[3][0])

# 12. Write a slice to extract [30, [40, 50, [60, 80, 90], 100, 110, 120]].
print(list2[2:4])

# 13.	Extract [100, 110, 120] from the nested sub-list [40, 50, [60, 80, 90], 100, 110, 120].
print(list2[3][3:])

# 14.	Write a slice to reverse the entire list2.
print(list2[::-1])

# 15.	Reverse the list [112, 114, 116].
print(list2[4][::-1])

# 16.	Write a slice to get [60, 80, 90].
print(list2[3][2:3])

# 17.	From the main list, extract [10, 30, [112, 114, 116]] using slicing.
print([list2[0], list2[2], list2[4]])

# 18.	Slice to extract [221, 226, 336] from the main list.
print(list2[5:])

# 19.	Write a slice to extract [40, 50, [60, 80, 90]].
print(list2[3][0:3])

# 20.	Write a slice to get [10, 30, [112, 114, 116], 226].
print([list2[0], list2[2], list2[4], list2[6]])

# 21.	How many elements are in list2[3] and list2[4]?
print(list2[3] ,list2[4])

# 22.	Write the statement to extract [112, 114, 116] from list2.
print(list2[4])

# 23.	Retrieve the element 80 from the third-level nested list [60, 80, 90].
print(list2[3][2][1])

# 24.	Access 110 using negative indexing.
print(list2[3][4])

# 25.	Extract the element 100 using a combination of indexes.
print(list2[3][3])

# 26.	Retrieve 90 from the list [60, 80, 90].
print(list2[3][2][2])

# 27.	Using negative indexing, extract 226 from list2.
print(list2[-2])

# 28.	What happens when you try list2[3][5][0]? Explain why.
print(list2[3][5][0])
#TypeError: 'int' object is not subscriptable 

# 29.	Retrieve the middle element 50 from [40, 50, [60, 80, 90], 100, 110, 120].
print(list2[3][1])

# 30.	Write statements to extract the first element (10) and the last element (336) of list2.
print([list2[0], list2[-1]])

# 31.	Retrieve 20 from list2 using both positive and negative indexing.
print(list2[1])
print(list2[-7])

# 32.	Write a slice to extract the first 4 elements of list2.
print(list2[:4])

# 33.	Slice to extract [30, [40, 50, [60, 80, 90], 100, 110, 120], [112, 114, 116]].
print(list2[2:5])

# 34.	Slice the main list to extract every second element.
print(list2[::2])

# 35.	Write a slice to reverse all elements in list2.
print(list2[::-1])

# 36.	Reverse [40, 50, [60, 80, 90], 100, 110, 120].
print(list2[3][::-1])

# 37.	Slice to get the last two sub-lists: [[112, 114, 116], 221, 226, 336].
print(list2[4:])

# 38.	Write a slice to extract [60, 80] from the list [60, 80, 90].
print(list2[3][2][:2])

# 39.	Slice to extract [50, [60, 80, 90], 100] from [40, 50, [60, 80, 90], 100, 110, 120].
print(list2[3][1:4])

# 40.	How many elements are in list2[3][2]?
print(len(list2[3][2]))

# 41.	Extract every second element from [40, 50, [60, 80, 90], 100, 110, 120] using slicing with a step.
print(list2[3][::2])

# 42.	Extract [80, 90] by combining indexing and slicing from [60, 80, 90].
print(list2[3][2][1:])

# 43.	Write a slice to reverse [60, 80, 90] using negative steps.
print(list2[3][2][::-1])

# 44.	Combine slicing and indexing to extract [50, 100, 120] from [40, 50, [60, 80, 90], 100, 110, 120].
print([list2[3][1], list2[3][3], list2[3][5]])

# 45.	Retrieve 50 and 80 in a single operation using slicing and indexing.
print(list2[3][1], list2[3][2][1])

# 46.	Reverse both [40, 50, [60, 80, 90], 100, 110, 120] and [112, 114, 116] in a single operation.
print([list2[3][::-1], list2[4][::-1]])