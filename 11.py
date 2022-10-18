# a python script to take the month value in numeric
# format and display the number of days in it.

# By using match case:

month = eval(input("Enter the month value in numeric: "))

match month:
    case 1:
        print("No. of days: 31")
    case 2:
        print("No. of days: 28(*29 days on leap years)")
    case 3:
        print("No. of days: 31")
    case 4:
        print("No. of days: 30")
    case 5:
        print("No. of days: 31")
    case 6:
        print("No. of days: 30")
    case 7:
        print("No. of days: 31")
    case 8:
        print("No. of days: 31")
    case 9:
        print("No. of days: 30")
    case 10:
        print("No. of days: 31")
    case 11:
        print("No. of days: 30")
    case 12:
        print("No. of days: 31")

# Or, Another method

print("\n Another Method: \n")

if month == 2:
    print("No. of days: 28(*29 days on leap years)")
elif month == 4 or month == 6 or month == 9:
    print("No. of days: 30")
else:
    print("No. of days: 31")
