import sys

def print_star(number):
    """this function get a number and print a pyramid """
    tmp = 1
    for i in range(1,number+1):
        print("* " * tmp)
        tmp += 1


try:
    user_input = int(input("Enter a number: "))
except ValueError:
    print("input not a number :\ ")
    sys.exit(1)


print_star(user_input)

sys.exit(0)