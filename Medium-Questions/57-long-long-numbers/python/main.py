import sys



def main():
    n = input("Enter a 30 digit Number:  ")
    if len(n) != 30:
        sys.exit("number Must be 30 characters")
    
    m = input("Enter a 30 digit Number:  ")
    if len(m) != 30:
        sys.exit("number Must be 30 characters")
    
    if not m.isdigit() or not n.isdigit:
        sys.exit("Input must be integer Number")

    # python is dynamic data type so this is not good for solving in python
    # but in other language like c c# and we should use correct type for variable to
    # calculate this otherwise it can be overflow
    print(int(m)+int(n))

if __name__ == '__main__':
    main()