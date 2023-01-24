import sys


def factorial(n):
    """
        this function get number and return factorial of it
    """
    if n == 1:
        return 1
    return n * factorial(n - 1)


def main():
    n = input("Enter a Number: ")
    try:
        n = int(n)
    except ValueError:
        sys.exit("Input Must be Integer")

    # iterate from 1 to n (Number that User enter)
    for i in range(1, n+1):
        # check value of factorial is equal to n or not
        if factorial(i) == n:
            print(f"Factorial of {i} is {n}")

if __name__ == '__main__':
    main()