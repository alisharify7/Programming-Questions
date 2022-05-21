import sys


def validate(number):
    """This Function validate user data"""
    
    try:
        # validate to user type number not int
        first_number = int(number[0])
        second_number = int(number[2])
    except ValueError:
        return False
    # check user type math operator
    if number[1] not in ["+", "-", "/", "*", "**"]:
        return False
    # return number in tuple mode
    return (first_number , second_number,)


# get input from user
user = input("Input : ").strip()

# create a list and split user data in it
num = []
num = user.split(" ")

# validate user date
if not validate(num):
    print("Invalid input")
    sys.exit(1)
else:
    # unpack tuple 
    f_number , sec_number = validate(num)


# if user type + 
if "+" in user:
    try:
        answer = f_number + sec_number
        print(f"Answer = {answer}")
        sys.exit(0)
    except Exception as e:
        # if math operator is Error 
        # print Error message
        print("Error ",e)
        sys.exit(1)


# if user type - 
if "-" in user:
    try:
        answer = f_number - sec_number
        print(f"Answer = {answer}")
        sys.exit(0)
    except Exception as e:
        print("Error ",e)
        sys.exit(1)


# if user type / 
if "/" in user:
    try:
        answer = f_number / sec_number
        print(f"Answer = {answer}")
        sys.exit(0)
    except Exception as e:
        print("Error ",e)
        sys.exit(1)

# if user type * 
if "*" in user:
    try:
        answer = f_number * sec_number
        print(f"Answer = {answer}")
        sys.exit(0)
    except Exception as e:
        print("Error ",e)
        sys.exit(1)

# if user type ** 
if "*" in user:
    try:
        answer = f_number ** sec_number
        print(f"Answer = {answer}")
        sys.exit(0)
    except Exception as e:
        print("Error ",e)
        sys.exit(1)