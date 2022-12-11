import os, sys

# t = 137486 x 225


def main():
    for x in range(1,10):
        if int(f"137486{x}225") % 7 == 0:
            print(x, end=" - ")

if __name__ == "__main__":
    main()
