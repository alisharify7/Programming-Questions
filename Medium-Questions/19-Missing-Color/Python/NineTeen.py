import sys

first = ["White", "Black", "Red"]
seccond = ["Red", "Green"]



for i in range(len(first)):
    temp = first[i]
    
    if (temp in seccond):
        continue
    else:
        print(temp)
        
