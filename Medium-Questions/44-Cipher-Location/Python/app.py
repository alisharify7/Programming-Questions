import os, sys, string

upper = " ".join(string.ascii_uppercase).split()
lower = " ".join(string.ascii_lowercase).split()


def find_loc(n):
    """
        this function return location of input in upper or lower list
    """
    n = n.strip()
    if n.isalpha():
        if n.isupper():
            return upper.index(n)
        if n.islower():
            return lower.index(n)


def cipher(char, key):
    """
        this function return cipher of input text => text
    """
    if char.isalpha():
        if char.islower():
            return lower[((find_loc(char) + key) % 26)] 
        if char.isupper():
            return upper[((find_loc(char) + key) % 26)] 
    return char


def main():
    message = input("Enter a Message: ")
    
    for index,value in enumerate(message):
        print(cipher(value, index), end="")


if __name__ == '__main__':
    main()