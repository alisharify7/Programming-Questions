import sys


def fibonacci(n):
    """
        this function get number and return fibonacci value of it
    """
    a = 0 
    b = 1 
    c = 0
    for i in range(n):
        c =  a + b
        a,b = b ,c
    
    return c
        

def main():
    n = input("Enter a Number: ")
    try:
        n = int(n)
    except ValueError:
        sys.exit("Input Must be Integer")

    print(f"{n}'s Number in Fibonacci Sequences is {fibonacci(n)}")



if __name__ == '__main__':
    main()