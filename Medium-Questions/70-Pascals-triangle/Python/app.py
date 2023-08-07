import os


def getBaseTriangle(size) -> list:
    n = [None] * size
    
    if len(n) >= 3:
        n[0] = 1
        n[-1] = 1

    if len(n) == 1:
        n[0] = 1

    elif len(n) == 2:
        n[0], n[1] = 1, 1

    return n



def makeThisLevel(level):
    response = str(11 ** level)
    temp = []
    for each in response:
        temp.append(each)
    return temp




def main():
    global data
    data = []

    x = int(input("level: "))
    plevel = 0
    for each in range(x):
        data.append(makeThisLevel(each))
    
    max_len = len(data[-1])
    for i in data:
        for j in i:
            space = max_len - len(i)
            print(" " * (space // 2), j, " " * (space //2), end="")
        print("")




if __name__ == "__main__":
    main()