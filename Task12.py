# # 	## List Method Practical ##

# 1. Create an empty list and use append() to add five different numbers to it. Print the final list.
list1 = []
list1.append(10)
list1.append(20)
list1.append(30)
list1.append(40)
list1.append(50)

print(list1)

# 2. Create a list of student name  and append a new Student name  and print the length of list .
student_name = ["Snehal","Amit","vishal"]
student_name.append("Priyanka")

print(student_name)
print(len(student_name))

# 3. Append a list [10, 20, 30] to another list and observe the result.
list2 = [2,4,6,8,10]
list2.append([10, 20, 30])
print(list2)

# 4. Create a list and make a copy using copy().
list3 = [1,3,5,7]
list4 = list3.copy()
print(list3)
print(list4)

# 5. Create a list with at least 10 elements, use clear(), and check the length of the list afterward.
list5 = [1,2,3,4,5,6,7,8,9,10]
list5.clear()
print(list5)
print(len(list5))

# 6. Create a nested list and clear only the inner list while keeping the outer list intact .
list6 = [1,2,3,[4,5,6,7],8,9,10]
list6[3].clear()
print(list6)

# 7. Given nums = [1, 2, 3, 4, 2, 2, 5, 2], find how many times 2 appears in the list.
nums = [1, 2, 3, 4, 2, 2, 5, 2]
print(nums.count(2))

# 8. Create a list of words and find how many times a particular word appears.
words = ["apple", "banana", "apple", "orange", "apple"]
print(words.count("apple"))

# 9. Create two lists, list1 in integer variable  and list2 in String variable. Use extend() to add elements of list2 to list1.     
#    Print the final result.
lis1 = [1,2,3,4,5]
lis2 = ["a","b","d","c"]
lis1.extend(lis2)
print(lis1)

# 10. Given fruits = ['apple', 'banana', 'cherry', 'banana', 'grape'], find the index of banana.
fruits = ['apple', 'banana', 'cherry', 'banana', 'grape']
print(fruits.index("banana"))

# 11. Insert the number 100 at the beginning of the list [10, 20, 30].
list = [10, 20, 30]
list.insert(0,100)
print(list)

# 12. Insert 'Python' at index 2 in a list of programming languages and print the result.
list = ["programming", "languages"]
list.insert(0,"Python")
print(list)

# 13. Given numbers = [5, 10, 15, 20, 25], remove and print the last element using pop().
numbers = [5, 10, 15, 20, 25]
numbers.pop()
print(numbers)

# 14. Remove an element at index 2 and print both the removed element and the updated list.
numbers1 = [5, 10, 15, 20, 25]
removed = numbers1.pop(2)
print(removed)
print(numbers1)

# 15. Given colors = ['red', 'blue', 'green', 'blue', 'yellow'], remove the first occurrence of 'blue'.
colors = ['red', 'blue', 'green', 'blue', 'yellow']
colors.remove("blue")
print(colors)

# 16. Reverse the list [1, 4, 9, 16, 25] and print the result.
list = [1, 4, 9, 16, 25]
list.reverse()
print(list)

# 17. Reverse a list of words and join them to form a sentence words = ["Hello", "world", "Python"].
words = ["Hello", "world", "Python"]
words.reverse()

sentence = "".join(words)
print(sentence)

# 18. Sort a list of numbers [10, 5, 8, 3, 1] in ascending and then in descending order.
numbers = [10, 5, 8, 3, 1]
numbers.sort()
print("Assending",numbers)
numbers.sort(reverse=True)
print("Descending",numbers)