import sys

def main():
    n = int(input())
    if not(n >= 2 and n <= (2*10**5) ):
        sys.exit(1)

    numbers = input().split()
    numbers = [int(each) for each in numbers]

    total_s = n * (n + 1) / 2
    print(int(total_s-sum(numbers)))


if __name__ == "__main__":    
    main()