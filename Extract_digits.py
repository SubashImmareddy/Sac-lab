s = input("Enter the string with digits:\n")
r = ""
for c in s:
    if c >= '0' and c <= '9':
        r += c + ","
print(r[:-1])
