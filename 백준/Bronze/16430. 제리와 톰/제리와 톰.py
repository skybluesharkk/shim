import fractions

a, b = map(int, input().split())

c = fractions.Fraction(a,b)
d = fractions.Fraction(1-c)
print(d.numerator,end=" ")
print(d.denominator)