import sys

def main():
    try:
        number = int(input("Enter a Number: "))
    except ValueError:
        print("Invalid Input ")
        sys.exit(1)

    print(f"Largest Number is {max(str(number))}")
    print(f"Smallest Number is {min(str(number))}")


if __name__ == "__main__":
    main()