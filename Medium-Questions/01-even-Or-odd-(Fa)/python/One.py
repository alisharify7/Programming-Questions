import sys

# defind a function for decied a Number
# is Even or odd

def is_valid(number):
    """ this Function take one Argument and if Number is Even Return true
    otherwise Return False"""
    if (number % 2 == 0):
        return True
    return False    

# get input from user
input_user = int(input("Enter Number: "))

# check for numbre between 1 to 100
if (input_user > 0 and input_user <= 100):
    
    # pass number to is_valid function for checking
    if (is_valid(input_user)):
        print("Even Number (valid)")
        sys.exit(0)
    else:
        print("Odd Number (Not valid)")    
        sys.exit(0)
else:
    print("input out of Range 1 to 100")


sys.exit(0)
