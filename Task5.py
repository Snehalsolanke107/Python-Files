													## Practices ##				

String1 = "Hello, World!"
# 	Extract "H"    
print(String1[0])
# 	Extract "Hello"   
print(String1[:5])
# 	Extract "World"
print(String1[-6:-1])
# 	Reverse the entire string
print(String1[::-1])

String2 = "Python Programming"
# 	Extract "Python"
print(String2[:6])
# 	Extract "Programming"
print(String2[7:18])
# 	Extract every alternate character 
print(String2[::2])

String3 = "Data Science and Machine Learning"
# 	Extract "Data"
print(String3[:4])
# 	Extract "Machine"
print(String3[-16:-9])
# 	Extract "Learning"
print(String3[-8:])

String4 = "1234567898521862120"
# 	Extract the first 5 digits and last 5 digits  
print(String4[:6])
print(String4[-5:])
# 	Extract the last 5 digits
print(String4[-5:])
# 	Extract all odd-indexed digits  
print(String4[1::2])

String5 = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
# 	Extract "ABCDEF"
print(String5[0:6])
# 	Extract every third letter
print(String5[2::3])
# 	Reverse the string
print(String5[::-1])

String6 = "Thequickbrownfoxjumpsoverthelazydog"
# 	Extract "quick"
print(String6[3:8])
# 	Extract "lazy dog"
print(String6[-7:-3]+" "+String6[-3:])
# 	Extract "thedog"
print(String6[25:28]+String6[-3:])


String7 = "abcdefghijklmn"
# 	Extract "def"
print(String7[3:6])
# 	Extract the last 4 characters
print(String7[-4:])
# 	Extract every second character starting from "a"
print(String7[::2])

String8 = "Sliceanddicestringseasily"
# 	Extract "Slice"
print(String8[0:5])
# 	Extract "dice"
print(String8[8:12])
# 	Reverse the words in the string
print(String8[::-1])