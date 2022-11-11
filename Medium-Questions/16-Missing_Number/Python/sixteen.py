import sys

def main():
    list = []
    user = input("Enter Number: ")
    # add user input to a list
    list = user.split(" ")

    # Find maximum value of input
    maximum = 0
    for i in range(len(list)):
        if (int(list[i]) > maximum):
            maximum = int(list[i])

    # print missing Numbers
    for i in range(1,maximum+1):
        if (str(i) not in list):
            print(i)

    
main()
sys.exit(0)