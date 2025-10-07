mylist = [1,2,3,4,5,6,7,8,9,10]

Snum = int(input("Enter a number to search for: "))


if Snum in mylist:
    index = mylist.index(Snum)
    print(f"Number {Snum} found at index {index}.")
else:
    print(f"Number {Snum} not found in the list.")
