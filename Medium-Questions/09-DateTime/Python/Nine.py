import time
import sys


x = time.localtime()
print("Current date and time is")
print(x[0],x[1],x[2],sep="-",end="  ")
print(x[3],x[4],x[5],sep=":")

sys.exit(0)