import sys

def is_valid(number):
    if (number % 2 == 0):
        return True
    return False    


input_user = int(input("Enter Number: "))    
if (input_user > 0 and input_user <= 100):
    if (is_valid(input_user) == True):
        print("Even number")
        sys.exit(0)
    else:
        print("Not even !")    
        sys.exit(0)
else:
    print("Not in range 1 - 100")


sys.exit(0)