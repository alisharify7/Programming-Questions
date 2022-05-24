import sys


# get input from user
user = input("Enter a string: ").strip()

# get middle of string and round it 
choice = round(len(user) / 2)

# print middle character and One character after it
print (user[choice],user[choice+1])
sys.exit(0)
