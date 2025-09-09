def quadratic_roots(a, b, c):
    d = b**2 - 4*a*c
    
    if d > 0:
        root1 = (-b + d**0.5) / (2*a)
        root2 = (-b - d**0.5) / (2*a)
        return f"Roots are real and distinct: {round(root1, 2)} and {round(root2, 2)}"
    
    elif d == 0:
        root = -b / (2*a)
        return f"Roots are real and equal: {round(root, 2)} and {round(root, 2)}"
    
    else:
        real_part = -b / (2*a)
        imaginary_part = ((-d)**0.5) / (2*a)
        real_part = round(real_part, 2)
        imaginary_part = round(imaginary_part, 2)
        return (f"Roots are complex: {real_part} + {imaginary_part}i and "
                f"{real_part} - {imaginary_part}i")

a = float(input("Enter coefficient a (not zero): "))
while a == 0:
    a = float(input("Coefficient a cannot be zero. Enter again: "))

b = float(input("Enter coefficient b: "))
c = float(input("Enter coefficient c: "))

print(quadratic_roots(a, b, c))
