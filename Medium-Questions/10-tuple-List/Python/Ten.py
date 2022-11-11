import sys

# create empty list and tuple
list_value = []
top = ()


user = input("Enter sequence of numbers with comma: ")

# split user input with <,> and store in list value
list_value = user.split(',')

# convert list to a tuple
top = tuple(list_value)

# print both tuple and list
print("LIST: ",list_value)
print("TUPLE: ",top)

sys.exit(0)