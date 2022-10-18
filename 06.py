# a python script to check whether a given number is a three digit number or not.

num = int(input("Enter Number: "))

if num > 99 and num <= 999:
    print("Your number is a three digit number")
else:
    print("Your number is not a three digit number")
