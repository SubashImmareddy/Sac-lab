r = int(input("Enter a number: "))

if r > 1:
    for i in range(2, int(r**0.5) + 1):
        if r % i == 0:
            print(r, "is not a prime number")
            break
    else:
        print(r, "is a prime number")
else:
    print(r, "is not a prime number")
