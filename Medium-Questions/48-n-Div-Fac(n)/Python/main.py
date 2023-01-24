import sys



def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n - 1)


def main():
    n = input("Enter a Number:")
    try:
        n = int(n)
    except ValueError:
        sys.exit("Input Must be Integer")

    print(f"Answer of 1 / {factorial(n)} ==> {1/factorial(n)}")


if __name__ == '__main__':
    main()