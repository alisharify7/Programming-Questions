import statistics as st
import sys


def validate(password):
    """this function return True if password match with condition 
    otherwise return False"""

    # check length of password
    if len(password) > 12 or len(password) < 8:
        return False

    # Rule (password should be created with alphabet or Numbers) 
    for each in password:
        if not each.isdigit() and not each.isalpha():
            return False
    return True

def Multipl_5(code):
    total = 0
    for each in code:
        if each % 5 == 0:
            total += each
    return total 



user = input('input a Password: ').lower().strip()
answer = validate(user)

if not answer:
    print('\n[Error]\n -Length of password must between 8 to 12\n -should all password created by Number or alphabet\n ')
    sys.exit(1)

code = list(map(lambda x: ord(x) ,user))
code.sort()
password = list(map(lambda x: x ,user))

# total of first element and last element and middle element
total_a = code[0] + code[-1] + round(st.mean(code))
total_5 =  Multipl_5(code)


if total_5 < total_a:
    print('Good Password')
    sys.exit(0)
elif total_5 > total_a:
    print('Bad Password')
    sys.exit(0)


print(code)
print(password)