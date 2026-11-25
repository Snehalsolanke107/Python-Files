	# 							## String Functions Practices ##
		
# 1. Write a Python program to convert the given string "hello world" to uppercase.
str1 = "hello world"
print(f"str1 : {str1}")
print(f"Use upper method : {str1.upper()}")

# 2. Convert the string "Python Programming" to lowercase.
str2 = "Python Programming"
print(f"str2 : {str2}")
print(f"Use lower method : {str2.lower()}")

# 3. Capitalize the first letter of "hello python learners".
str3 = "hello python learners"
print(f"str3 : {str3}")
print(f"Use Capitalize method : {str3.capitalize()}")

# 4. Convert "welcome to python" to title case.
str4 = "welcome to python"
print(f"str4 : {str4}")
print(f"Use title method : {str4.title()}")

# 5. Remove leading and trailing spaces from the string " Python String Functions " using strip().
str5 = " Python String Functions "
print(f"str5 : {str5}")
print(f"Use strip method : {str5.strip()}")

# 6. Remove only trailing spaces from "Hello World ".
str6 = "Hello World "
print(f"str6 : {str6}")
print(f"Use rstrip method : {str6.rstrip()}")

# 7. Remove only leading spaces from " Learn Python".
str7 = " Learn Python"
print(f"str7 : {str7}")
print(f"Use lstrip method : {str7.lstrip()}")

# 8. Split the string "apple banana grape" into a list using split().
str8 = "apple banana grape"
print(f"str8 : {str8}")
print(f"Use split method : {str8.split()}")

# 9. Join the list ['Python', 'is', 'fun'] into a single string using join() with space as a separator.
str9 = ['Python', 'is', 'fun']
print(f"str9 : {str9}")
print(f"Use join method : {str9.join()}")

# 10. Convert the list ['A', 'B', 'C'] into a single string "A-B-C" using join().
str10 = ['A', 'B', 'C']
print(f"str10 : {str10}")
print(f"Use join function : {'-'.join(sorted(str10))}")

# 11. Find the index of the first occurrence of "Python" in "I love Python programming".
str11 = "I love Python programming"
print(f"str11 : {str11}")
rint(f"Occurance text : Python")
print(f"Use find method : {str11.find('Python')}")

# 12. Find the last occurrence of "o" in "Hello World".
str12 = "Hello World"
print(f"str12 : {str12}")
rint(f"Occurance word : o")
print(f"Use  rfind method : {str12. rfind('o')}")

# 13. Replace "Java" with "Python" in the string "I love Java".
str13 = "Java"
print(f"str13 : {str13}")
print(f"Replace text : Hello")
print(f"Use replace method : {str13.replace('Java','Python')}")

# 14. Check if the string "Hello World" starts with "Hello".
str14 = "Hello World"
print(f"str14 : {str14}")
print(f"find with : Hello")
print(f"Use startswith method : {str14.startswith('Hello')}")

# 15. Check if the string "example.txt" ends with ".txt".
str15 = "example.txt"
print(f"str15 : {str15}")
print(f"find text : .txt")
print(f"Use endswith method : {str15.endswith('.txt')}")

# 16. Count the occurrences of "o" in "Hello, how are you?".
str16 = "Hello, how are you?"
print(f"str16 : {str16}")
print(f"Occurance word : o")
print(f"Use Count method : {str16.count('o')}")

# 17. Find the index of "r" in "programming".
str17 = "programming"
print(f"str17 : {str17}")
print(f"find index of : r")
print(f"Use index method : {str17.index('r')}")

# 18. Try finding the index of "z" in "python" using index(), and observe the error.
str18 = "python"
print(f"str18 : {str18}")
print(f"find index of : z")
print(f"Use find method : {str18.find('z')}")

# 19. find the last occurrence of "e" in "experience".
str19 = "experience"
print(f"str19 : {str19}")
print(f"Occurance word : e")
print(f"Use rfind method : {str19.rfind('e')}")

# 20. find the first occurrence of "e" in "experience".
str20 = "experience"
print(f"str20 : {str20}")
print(f"Occurance word : e")
print(f"Use find method : {str20.find('e')}")

# 21. Check if the string "Python" contains only alphabets.
str21 = "Python"
print(f"str21 : {str21}")
print(f"Use isalpha method : {str21.isalpha()}")

# 22. Verify if "12345" contains only digits.
str22 = "12345"
print(f"str22 : {str22}")
print(f"Use isdigit method : {str22.isdigit()}")

# 23. Check if "Python123" is alphanumeric.
str23 = "Python123"
print(f"str23 : {str23}")
print(f"Use isalphanumeric method : {str23.isalphanumeric()}")

# 24. Test if the string " " consists of only spaces.
str24 = " "
print(f"str24 : {str24}")
print(f"Use isspace method : {str24.isspace()}")

# 25. Check if "12345" is numeric using.
str25 = "12345"
print(f"str25 : {str25}")
print(f"Use isnumeric method : {str25.isnumeric()}")

# 26. Use format() to insert "Python" and "fun" into the string "{} is {}!".
str26 = "{} is {}!"
print(f"str26 : {str26}")
print(f"Use Format method : {str26.format('Python', 'fun')}")

# 27. Partition the string "python-programming-language" at "-".
str27 = "python-programming-language"
print(f"str27 : {str27}")
print(f"Partition occurs with : -")
print(f"Use Partition method : {str27.partition('-')}")

# 28. Use rpartition() to split "one-two-three" from the right sing "-".
str28 = "one-two-three"
print(f"str28 : {str28}")
print(f"Partition occurs with : -")
print(f"Use rpartition method : {str28.rpartition('-')}")

# 29. Convert "PYTHON" to lowercase using casefold().
str29 = "PYTHON"
print(f"str29 : {str29}")
print(f"Use casefold method : {str29.casefold()}")

# 30. Convert "42" into a 5-character string padded with zeros using zfill().
str30 = "42"
print(f"str30 : {str30}")
print(f"Use zfill method : {str30.zfill(42)}")

# 31. Check if "HELLO" is in uppercase.
str31 = "HELLO"
print(f"str31 : {str31}")
print(f"Use isupper method : {str31.isupper()}")

# 32. Verify if "hello" is in lowercase.
str32 = "hello"
print(f"str32 : {str32}")
print(f"Use islower method : {str32.islower()}")

# 33. Check if "Python Programming" follows title case.
str33 = "Python Programming"
print(f"str33 : {str33}")
print(f"Use istitle method : {str33.istitle()}")

# 34. Sort the characters of "banana" alphabetically.
str34 = "banana"
print(f"str34 : {str34}")
print(f"Use sorted function : {''.join(sorted(str34))}")

# 35. Find the length of the string "Data Science".
str35 = "Data Science"
print(f"str35 : {str35}")
print(f"Use len Method : {len(str35)}")

# 36. Sort the characters of "The Kiran  Academy" alphabetically in descending Order.
str36 = "The Kiran  Academy"
print(f"str36 : {str36}")
print(f"Use join method for Characters in descending order : {''.join(sorted(str36, reverse=True))}")