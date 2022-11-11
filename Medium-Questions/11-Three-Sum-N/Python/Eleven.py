import sys

list = []

# get input from user but in string format
user = input("Enter an integer: ")

# add user input to a list to can multiple on string
for i in range(1,4):
    list.append(user * i)


sum = 0
# interate on list and get sum of the list
for i in range(len(list)):
    sum += int(list[i])


print(sum)
sys.exit(0)

