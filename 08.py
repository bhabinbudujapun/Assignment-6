# a python script to check whether a given quadratic equation has two real &
# distinct roots, real & equal roots or imaginary roots

# Asking for the value of a,b and c from user

a = int(input("Enter the value for 'a': "))
b = int(input("Enter the value for 'b': "))
c = int(input("Enter the value for 'c': "))

# Value of 'Discriminant

D = b ** 2 - 4 * a * c

# Nature of roots of quadratic equation

if D == 0:
    print("Nature of the Roots: Real and Equal roots")
elif D > 0:
    print("Nature of the Roots: Real and Unequal roots")
else:
    print("Nature of the Roots: No Real roots")
