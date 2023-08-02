import os


def main():
    x = input("Enter Input: ")
    x = x.split(" ")
    x.reverse()
    answer = " ".join(x)
    print(answer)


if __name__ == "__main__":
    main()