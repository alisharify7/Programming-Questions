import sys



def main():
    n = input("Enter a Number:  ")
    if not n.isdigit():
        sys.exit("Input Must a Number ")

    # convert str to int
    n = int(n)
    
    print(f"\n-{n} in bin<2> is {bin(n)}")
    print(f"-{n} in hex<16> is {hex(n)}")
    print(f"-{n} in oct<8> is {oct(n)}\n")

if __name__ == '__main__':
    main()