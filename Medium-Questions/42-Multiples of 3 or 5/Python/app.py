import os

def is_ok(n):
    """
        this function take number and return a Boolean
        and check if input number is multiple of 5 or 3
    """
    return (n % 3 == 0 or n % 5 == 0)



def main():

    result = 0
    # iterate over all numbers
    for i in range(1000):
        # check for multiple of 5 or 3
        if is_ok(i):
            # if its ok
            result += i

    print(f"sum of all the multiple of 5 or 3 below 100 is {result}")



if __name__ == '__main__':
    main()