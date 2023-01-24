import os, sys

def main():
    n = input("Enter a/b : ")
    m = input("Enter d/c : ")
    try:
        
        a = (n.strip().split("/"))[0]
        b = (n.strip().split("/"))[-1]
        d = (m.strip().split("/"))[0]
        c = (m.strip().split("/"))[-1]
        
        a = int(a)
        b = int(b)
        d = int(d)
        c = int(c)

        print(round(a//b) / round(d//c))
    except (ValueError, IndexError):
        sys.exit("Input Must be Integer")
    

if __name__ == "__main__":
    main()