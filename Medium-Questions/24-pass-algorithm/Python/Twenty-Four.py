import statistics as st
import sys
import colorama as color
import random

color.init()

def validate(password):
    """this function return True if password match with condition otherwise return False"""

    # check length of password
    if len(password) > 12 or len(password) < 8:
        return False

    # Rule (password should be created with alphabet or Numbers) 
    for each in password:
        # check if i is not number of alphabet so return false
        if not each.isdigit() and not each.isalpha():
            return False
    return True


def Multipl_5(code):
    """ this function return Number of element in a list that multiple of 5 """
    total = 0
    for each in code:
        if each % 5 == 0:
            total += each
    return total 


# get input from user
user = input('input a Password: ').lower().strip()
answer = validate(user)

# check answer returned from function
if not answer:
    print('\n[Error]\n -Length of password must between 8 to 12\n -should all password created by Number or alphabet\n ')
    sys.exit(1)

# add all password character ascii code in code array list
code = list(map(lambda x: ord(x) ,user))
code.sort()

# add all characters of user input in password array list
password = list(map(lambda x: x ,user))


location_middle = round(len(code) / 2)
# total of first element and last element and middle element
total_a = code[0] + code[-1] + code[location_middle]
total_5 =  Multipl_5(code)


if total_5 < total_a:
    print('Good Password')
    sys.exit(0)
elif total_5 > total_a:
    print('Bad Password')
    sys.exit(0)
else:
    rand = random.randint(0,len(password))
    print(rand)
    print(f"{color.Fore.BLUE}{user}")
    sys.exit(0)

