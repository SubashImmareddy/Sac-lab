mylist = [1,2,3,4,5,6,7,8,9,10]

Snum = int(input("Enter a number to search for: "))

found = False
for i in range(len(mylist)):
    if mylist[i] == Snum:
        print(f"Number {Snum} found at index {i}.")
        found = True
        break 

if not found:
    print(f"Number {Snum} not found in the list.")
