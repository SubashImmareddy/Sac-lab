pi = 3.14
def circumfrence_area(r):
 circumfrence = 2*pi*r
 area = pi*r*r
 return circumfrence,area

r = float(input("Enter the radius:\n"))
c,a = circumfrence_area(r)

print("Circumference: {:.2f}".format(c))
print("Area: {:.2f}".format(a))