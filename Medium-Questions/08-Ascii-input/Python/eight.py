import sys

# get input from user
tmp = input("Enter character: ")

# get ascii value of character
tmp = ord(tmp)

# if tmp between 48 to 57 so user input is number
if (tmp >= 48 and tmp <= 57):
    print("number")
    sys.exit(0)

# if tmp between 65 to 90 so user input is number
elif(tmp >= 65 and tmp <= 90):
    print("upper case alphbet")
    sys.exit(0)
    
# if tmp between 97 to 122 so user input is number
elif(tmp >= 97 and tmp <= 122):
    print("Lower case alphabet")        
    sys.exit(0)
    
else:
    print("its a symbol")
    sys.exit(0)

    # ascii table 
# https://www.asciitable.com/asciifull.gif 
