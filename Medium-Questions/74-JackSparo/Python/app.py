import sys

"""
https://quera.org/problemset/234249
"""

def get_int(msg=""):
    x = input(msg)
    if not x.isdigit(): 
        sys.exit("input must be a number")

    return int(x)

def main():
    numbers = input().split()
    if len(numbers) != 7 :
        sys.exit("length of numbers must be 7")
    

    for index,value in enumerate(numbers):
        if not value.isdigit():
            sys.exit("number must be a digit")
        numbers[index] = int(value)

    n = get_int()
    if n > 7 or n < 1:
        sys.exit("invalid number, n must between 1 and 7")
    
    
    index = numbers.index(n)
    len_before = len(numbers)
    numbers = numbers[:index]

    print(len_before-len(numbers))


if __name__ == '__main__':
    main()