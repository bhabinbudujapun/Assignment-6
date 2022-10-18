# a python script to accept one complex number from the
# user and display the greater number between real part and imaginary part

real = eval(input("Enter real part: "))
imaginary = eval(input("Enter imaginary part: "))

# converting into complex number

z = complex(real, imaginary)

print("complex number: ", z)

# comparing between reap part and imaginary part

if real > imaginary:
    print("Greater number: real part")
else:
    print("Greater number: imaginary part")
