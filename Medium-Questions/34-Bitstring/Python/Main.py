import sys


try:
    n = int(input("Enter n: "))
except ValueError:
    print("Invalid input")
    sys.exit(1)

if n >=1 and n <= 106:
    print(2**n)
else:
    print("Out of Range")


