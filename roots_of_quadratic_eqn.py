x = int(input("Enter the coefficient of x^2: "))
y = int(input("Enter the coefficient of x: "))
z = int(input("Enter the constant term: "))

d = y**2 - 4*x*z

if d > 0:
    r1 = round((-y + d**0.5) / (2*x), 4)
    r2 = round((-y - d**0.5) / (2*x), 4)
    print("The roots are real and distinct and are:", r1, "and", r2)

elif d == 0:
    r1 = round(-y / (2*x), 4)
    print("The roots are real and equal and is:", r1)

else:
    real = round(-y / (2*x), 2)
    imag = round(abs(d)**0.5 / (2*x), 2)
    print("The roots are imaginary.")
    print("The roots are:", real, "+", imag, "i and", real, "-", imag, "i")
