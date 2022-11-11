import sys


binary_pow = []

try:
    user = int(input('Enter Number: '))
    if user < 0:
        print('Enter a positive Number :( ')
        sys.exit(1)
except ValueError:
    print("It's Not a Number")
    sys.exit(1)



i = 0
while True:
    temp =2**i
    binary_pow.append(temp)
    i+=1
    if temp > user:
        break

binary_pow.reverse()

for i in binary_pow:
    if user >= i:
        user -= i
        print("1",end='')
    else:
        print("0",end='')