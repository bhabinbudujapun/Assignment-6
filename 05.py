#  a python script to print two given words in dictionary order

num1 = int(input("Enter a first Number: "))
num2 = int(input("Enter a second Number: "))

if num1 > num2:
    print("Dictionary order: ", num2, num1, sep=" ")
else:
    print("Dictionary order: ", num1, num2, sep=" ")
