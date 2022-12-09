import sys


def get_maqsom(n):
    result = []
    for i in range(1, 10000):
        counter = 0
        for j in range(1, int(i / 2) + 1):
            if i % j == 0:
                counter += 1
                if counter == n:
                    result.append(i)
                if counter > n:
                    if i in result:
                        result.remove(i)
                    
    return result



def main():
    n = input("Enter Number of divisible:  ")
    try:
        n = int(n)
    except ValueError:
        sys.exit("input must be integer ")

    result = get_maqsom(n)
    for each in result:
        print(each, end="  ")

if __name__ == '__main__':
    main()