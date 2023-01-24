import sys



def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n - 1)


def main():
    f = input("Enter First Number:")
    try:
        f = int(f)
    except ValueError:
        sys.exit("Input Must be Integer")
    
    s = input("Enter Second  Number:")
    try:
        s = int(s)
    except ValueError:
        sys.exit("Input Must be Integer")

    result = 0
    for i in range(f):
        result += s

    print(result)


if __name__ == '__main__':
    main()