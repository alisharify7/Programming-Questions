import sys

# get input from user
user = input("Enter ip: ")

# defind a list for add ip address to it
names = []
# split user input and add it to list
names = user.split(".")

# interate over all list
for i in names:
    # try to confirm user input is a int not string
    try:
        i = int(i)
        if i > 0 and i  < 255:
            continue
        else:
            # if user input ip is out on range
            print("Invalid ip Address")
            sys.exit(1)
    # if user input is a string quit
    except ValueError:
        print('It\'s Not a Number :( ') 
        sys.exit(1)

# if every this goes fine!
print('Correct ip address') 
