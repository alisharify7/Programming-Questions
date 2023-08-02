import os

def get_int(message:str) -> int:
    while  True:
        x = input(message)
        try:
            x = int(x)
        except ValueError:
            continue
        else:
            return x


def main():
    x = get_int("enter number: ")
    for i in range(1, x+1):
        for j in range(1, x+1):
            print(j*i, end=" ")
        print("")



if __name__ == "__main__":
    main()