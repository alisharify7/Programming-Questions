import sys

def bin_digit(number):
    """first conver a int to binary then return number of one in binary Value"""
    counter = 0
    number = bin(number)
    length = len(number)

    for one in range(length):
        if (number[one] == '1'):
            counter += 1

    return counter        

try:
    user = int(input("user: "))
except ValueError:
    print("its not a number")
    sys.exit(1)


print(bin_digit(user))
sys.exit(0)
