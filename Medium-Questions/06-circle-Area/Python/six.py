import sys
import math

r = float(input("Enter r: "))

# formula for calculate radius of circle 
# c = 2pr
# https://www.wikihow.com/Calculate-the-Radius-of-a-Circle


p = math.pi

answer = p * (r ** 2)

print("Area: ",answer)

sys.exit(0)
