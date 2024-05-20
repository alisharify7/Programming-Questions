import sys

"""
1 <= n <= 2.10^5
1 <= x_i <= 10^9
"""


def main():
    n = int(input())

    # if (n < 1 or n >= (2 * (10 ** 5))): # n
    #     sys.exit("Invalid input n")

    numbers = input()
    numbers = numbers.split()

    if len(numbers) != n:
        sys.exit("length of numbers must be equal to n")

    # for each in numbers:
    #     each = int(each)
    #     if (1 >= each or each >= 10**9):
    #         sys.exit("Invalid input x must be between 1 and 10**9") 


    numbers_bank = set(numbers) 
    # set removes duplicates numbers automatically
    print(len(numbers_bank))


if __name__ == '__main__':
    main()
