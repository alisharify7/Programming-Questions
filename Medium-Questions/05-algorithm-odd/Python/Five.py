import sys

def is_even(number):
    if (number % 2 == 0):
        return True
    return False    


n = int(input())
if (n < 0):
    print("Number must be positive :(")
    sys.exit(1)

print(n,end=" " )

while (True):
    if (n == 1):
        sys.exit(0)

    if (is_even(n)):
        n //= 2
        print(n,end=" ")
        continue

    n *= 3
    n += 1     
    print(n,end=" ")







