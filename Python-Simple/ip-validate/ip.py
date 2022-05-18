import sys


user = input("Enter ip: ")

names = []
names = user.split(".")


for i in names:
    try:
        i = int(i)
        if i > 0 and i  < 255:
            continue
        else:
            print("Invalid ip Address")
            sys.exit(1)
    except ValueError:
        print('It\'s Not a Number :( ') 
        sys.exit(1)

print('Correct ip address') 
