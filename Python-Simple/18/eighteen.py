import sys

def cube_number(number):
    """return sum of the positive number that given to function"""
    sum_cube = 0
    for i in range(1,number):
        sum_cube += i ** 3

    return sum_cube




def main():
    try:
        user = int(input("Enter a positive number: "))
    except ValueError:
        print("That's not a number :( ")
        sys.exit(0)

    if(user <= 0):
        print("That's not a Positive number'")         
        sys.exit(1)
    else:
        resualt = cube_number(user)
        print("resualt is => %i" % resualt)

main()