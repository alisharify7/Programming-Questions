import sys

# get input from user
name = input("name : ")
last_name = input("last name : ")

# get len of inputs
len1 = len(last_name)
len2 = len(name)

# interate in last name string
for i in range(len1-1,-1,-1):
    print(last_name[i],end="")
    print(" ",end="")
  
# interate in name string 
for i in range(len2-1,-1,-1):
    print(name[i],end="")
    print(" ",end="")


sys.exit(0)    