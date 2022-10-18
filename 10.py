# a python script to print greater among three numbers.
# Print number only once even if the numbers are the same.

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

if a < b:
    if c < b:
        print("Greater number: ", b)
    else:
        print("Greater number: ", c)
elif a < c:
    print("Greater number: ", c)

else:
    print("Greater number: ", a)
