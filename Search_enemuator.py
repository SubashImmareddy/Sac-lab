mylist = [1,2,3,4,5,6,7,8,9,10]

Snum = int(input("Enter a number to search for: "))

found = False
for index, value in enumerate(mylist):
    if value == Snum:
        print(f"Number {Snum} found at index {index}.")
        found = True
        break  

if not found:
    print(f"Number {Snum} not found in the list.")
