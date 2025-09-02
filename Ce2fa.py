def c_2_f(c):
    return c+273
c = int(input("Enter the celsius:\n"))
c=c_2_f(c)
print(f"{round(c,2)} in Farenheit")