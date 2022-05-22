import sys

def search(number):
    counter_19 = 0
    counter_5 = 0
    
    for i in number:
        i = i.strip()
    
        if (i == '19'):
            counter_19 += 1
            continue

        if (i == '5'):
            counter_5 += 1
            continue
    
    if counter_19 == 2 and counter_5 >= 3:
        return True
    return False



user = input("Input: ").strip()
user = user.split(",")
answer = search(user)

if answer:
    print("True")
    sys.exit(0)
else:
    print("False")
    sys.exit(1)