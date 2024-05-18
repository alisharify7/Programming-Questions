import sys


"""
dimensions =  𝑛×(2𝑛−1)
each line = 2*n-1
https://quera.org/problemset/220669

dimensions: 8*(2*n-1)
max = 8 * 2 - 1
in: 8
.......D.......
......D.D......
.....D...D.....
....D.....D....
...D.......D...
..D.........D..
.D...........D.
D.D.D.D.D.D.D.D

in: 3
..D..
.D.D.
D.D.D

"""


def main():
    n = int(input(""))
    if n > 20 or n < 3:
        sys.exit("Invalid n")

    M_CHAR = (n * 2) - 1

    for i in range(n):

        for before in range(i, (M_CHAR//2)):  # before
            print(".", end="")

        for inner in range((M_CHAR//2)-i, n):
            if i == n-1:
                if inner == 0:
                    print("D.", end="")
                elif inner == n-1:
                    print("D", end="")
                else:
                    print("D.", end="")
            else:
                if inner == (M_CHAR//2)-i and i != 0:
                    print("D.", end="")
                elif inner == n-1:
                    print("D", end="")
                else:
                    if inner != 0:
                        for dot in range(2):
                            print(".", end="")
                    else:
                        print(".", end="")

        for after in range(i, (M_CHAR//2)):  # after
            print(".", end="")

        print()


if __name__ == '__main__':
    main()
