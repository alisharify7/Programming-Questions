import os

def factorial(n):
    """
        This function take an number and 
        return factorial of that number
    """
    if n == 1:
        return 1

    return factorial(n - 1) * n 


def radical(n):
    """
        this function take an number and return 
        radical of that number
    """
    return n ** 0.5


def get_int(msg):
    """
        this function only return integer number
    """
    while True:
        n = input(msg)
        try:
            n = int(n)
        except ValueError:
            continue
        else:
            return n


def main():
    # get number from user
    number = get_int("Enter a Number: ")
    result = 0
    for each in range(1,number+1):
        result += (radical(each) / each) - (factorial(each) / (each ** 2))

    print(result)


if __name__ == '__main__':
    main()
