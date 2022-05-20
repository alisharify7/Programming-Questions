
import sys

user_input = int(input("Enter a number: "))
if user_input <= 0:
    print("Negetive number !\n")
    sys.exit(1)
else:    
    for i in range(user_input):
        print("*")

sys.exit(0)        