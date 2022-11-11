import sys

n = int(input("Enter n: "))

# @ hard code way
# ans = 0
# for i in range(n+1):
#     ans +=i
# print(ans)    

# @ mathematical way
answer = (n * (n+1) / 2)
print(answer)
    

sys.exit(0)    