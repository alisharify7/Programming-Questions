import sys

# this function check is a number is even or not
def is_even(number):
    if (number % 2 == 0):
        return True
    return False    


# get input and check is positive number or not 
n = int(input("Enter numbr: "))
if (n < 0):
    print("Number must be positive :(")
    sys.exit(1)

# infinity loop because if number is big we had keep going to number equal to one
while (True):
    # print number each time
    print(f"Number is {n}")

    # send number to even function and if number is even so we divided by 2
    # and continue this loop
    if (is_even(n)):
        n //= 2
        continue
    # else we just multiplies it by 3 and add 1 to it
    n *= 3
    n += 1     






