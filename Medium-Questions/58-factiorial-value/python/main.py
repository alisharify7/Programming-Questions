import sys


def factorial(n):
    if n == 1:
        return 1

    return n * factorial(n -1 )

def main():
    n = input("Enter a Number:  ")
    try:
        n = int(n)
    except ValueError:
        sys.exit("input must be integer ")

    print(f"Factorial value is : {factorial(n)}")
if __name__ == '__main__':
    main()