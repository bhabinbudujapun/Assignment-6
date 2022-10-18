# a python script to check whether a given year is a leap year or not.

year = int(input("Enter the year: "))

if year % 400 == 0:
    print("Leap Year")
else:
    if year % 4 == 0 and year % 100 != 0:
        print("Leap Year")
    else:
        print("Non-Leap Year")
