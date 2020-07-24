from math import sqrt
from fractions import Fraction

print ("Factor and Solve a Quadratic Polynomial")
print ("ax^2+bx+c=0")
a = int(input("a = "))
b = int(input("b = "))
c = int(input("c = "))

discriminant = (b ** 2) - (4 * a * c)

if discriminant < 0:
    print("Cannot be factored and has no real roots.")
else:
    y = sqrt(discriminant)

    root1 = (-b + y) / (2 * a)
    root2 = (-b - y) / (2 * a)

    frac_root1 = Fraction(root1).limit_denominator()
    frac_root2 = Fraction(root2).limit_denominator()
    a = frac_root1.denominator
    b = frac_root1.numerator * -1
    c = frac_root2.denominator
    d = frac_root2.numerator * -1

    print ("Factorized: (%dx%+d)(%dx%+d)" % (a, b, c, d))
    print ("x = %.2f or x = %.2f" % (root1, root2))
