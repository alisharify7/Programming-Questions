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

    while True:
        try:
            x = int(input("level: "))
        except ValueError:
            continue
        else:
            break
    plevel = 0
    for each in range(x):
        data.append(makeThisLevel(each))
    
    max_len = len(data[-1])
    for index, i in enumerate(data):
        space = max_len - len(i)
        print(f"[{index}]", end=" ")
        print(" " * ((space // 2 +1 )), "".join(i), " " * (space //2 +1), end="")
        print("")

        # normal print
    # for each in data:
    #     print(" ".join(each))



if __name__ == "__main__":
    main()