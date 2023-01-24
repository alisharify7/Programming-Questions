import sys



def main():
    n = input("Enter a binary Number:  ")
    m = n
    # convert str to int
    try:
        n = int(n, base=2)
    except ValueError:
        sys.exit("invalid input")

    print(f"\n-{m} in int<10> is {n}")
    print(f"-{m} in hex<16> is {hex(n)}")
    print(f"-{m} in oct<8> is {oct(n)}\n")

if __name__ == '__main__':
    main()