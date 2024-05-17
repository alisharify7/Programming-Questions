def main():
    n = int(input("enter n:"))
    numbers = input("enter numbers:")
    numbers_bank = set(numbers.split())
    print(len(numbers_bank))


if __name__ == '__main__':
    main()
