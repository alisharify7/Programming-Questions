import sys



def main():
    n = input("Enter a Number sequences: ")
    if not n.isdigit():
        sys.exit("Input Must a Number Sequences")
    # reverse str input
    n = n[::-1]
    
    # convert str input to int
    print(f"\nAnswer is => {int(n)} and answer Type is {type(int(n))}\n")


if __name__ == '__main__':
    main()