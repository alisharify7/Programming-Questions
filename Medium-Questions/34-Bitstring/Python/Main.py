import sys
import random

# possible value for each bit
values = [0,1]

# define a set(because skip duplicate value)
chance = set()

# get input form user
n = int(input("Enter NUmber of Bits: "))

if n >= 1 or n <= 106: 
    # all change is n * n
    for i in range(n*n):
        # in each chance we create possible bit
        for i in range(n):
            # value of first bit 
            rand1 = random.randint(0,1)
            # value of seccond bit 
            rand2 = random.randint(0,1)
            # value of third bit 
            rand3 = random.randint(0,1)

            # add it to set
            chance.add((rand1,rand2,rand3))

    print(f"we have {len(chance)} chance".title())
    print(f"chance Are:".title())
    for i in chance:
        print(i)
