import sys


def main():
    n = input("Enter Number of round:  ")
    try:
        n = int(n)
    except ValueError:
        sys.exit("input must be integer ")

    numbers = []
    
    i = 0
    while True:
        if i == n:
            break
        temp = input(f"Enter Number \33[33m{i+1}\33[0m: ")

        try:
            temp = float(temp)
        except ValueError:
            print("invalid input :(")
            continue
        else:
            numbers.append(temp)
            i += 1
    

    print(f"\33[32mmaximum value is {max(numbers)}")
    print(f"minimum value is {min(numbers)}")
    print(f"average value is {sum(numbers) / len(numbers)} \33[0m")

if __name__ == '__main__':
    main()
