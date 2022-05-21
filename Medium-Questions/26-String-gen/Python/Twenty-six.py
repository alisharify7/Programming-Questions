import sys
import random


character= []
user = input("Enter a String: ")

for each in user:
    character.append(each)


chance = len(character) * len(character)
flag = 0
res = ''

rand_string = []
while True:
    if flag == chance:
        break
    
    for i in user:
        temp= []
        rand = random.choice(character)
        temp.append(rand)
    
    for each in temp:
        res += character[each]


    if res not in rand_string:
        rand_string.append(res)
        res = ''
    else:
        flag += 1
        continue


print(len(rand_string))
print(rand_string)