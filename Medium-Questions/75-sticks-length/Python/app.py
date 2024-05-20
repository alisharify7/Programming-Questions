import sys

def main():
    n = int(input())
    sticks = input().split()
    if len(sticks) != n:
        sys.exit("Invalid n")

    sticks = [int(each) for each in sticks]
    sticks.sort()
    medianINDEX = len(sticks)//2
    median = sticks[medianINDEX]
    cost = 0
    for index, value in enumerate(sticks):
        if index == medianINDEX:
            continue
        cost += abs(value-median)

    print(cost)

if __name__ == '__main__':
    main()