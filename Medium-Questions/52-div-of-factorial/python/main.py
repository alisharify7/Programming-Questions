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

    result = 0
    # iterate from 1 to n (Number that User enter)
    for i in range(1, n+1):
        result += i / factorial(i)
        
        if i == (n):
            print(f"({i} / {i}!)", end=" ")
        else:        
            print(f"({i} / {i}!)", end="\33[32m + \33[0m")

    print(f"\33[31m = \33[0m {result} ")

    for i in range(1, n+1):        
        if i == (n):
            print(f"({i} / {factorial(i)})", end=" ")
        else:        
            print(f"({i} / {factorial(i)})", end="\33[32m + \33[0m")

    print(f"\33[31m = \33[0m {result} ")

if __name__ == '__main__':
    main()