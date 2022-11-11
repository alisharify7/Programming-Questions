import sys

def ev(number):
    if number % 2 == 0:
        return True
    return False


try:    
    user = int(input("Enter Number of Piles: ").strip())
except ValueError:
    print("Please Enter a Number")
    sys.exit()

pil = []

if ev(user):
    pil.append(user)
    for i in range(user):
        pil.append(pil[i] + 2)
    pil.pop()
else:
    pil.append(user)
    for i in range(user):
        pil.append(pil[i] + 2)
    pil.pop()

print(pil)
