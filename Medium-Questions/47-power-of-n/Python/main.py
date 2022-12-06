import sys


def main():
    n = input("Enter a Number:")
    try:
        n = int(n)
    except ValueError:
        sys.exit("Input Must be Integer")

    for i in range(n+1):
        print(f"2^{i} = \33[32m {2**i}\33[0m")


if __name__ == '__main__':
    main()