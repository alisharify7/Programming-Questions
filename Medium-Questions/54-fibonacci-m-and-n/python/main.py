import sys


def fibonacci(m, n):
    """
        this function get number and return fibonacci value of it
    """
    a = 0 
    b = 1 
    c = 0
    result = []
    for i in range(m):
        c =  a + b
        a,b = b ,c
        result.append(c)
        if c > m+n:
            break
    
    if m in result:
        index = result.index(m)
        try:
            if result[index - 1] == n:
                print("\33[34mSequence is =>\33[0m ")
                for each in result:
                    if each == n:
                        print(f"\33[32m {each} \33[0m", end=" ")
                    elif each == m:
                        print(f"\33[32m {each} \33[0m", end=" ")
                    else:
                        print(each, end=" ")

                return True
        except IndexError:
            return False
    
    return False
        

def main():
    n = input("Enter N Number: ")
    try:
        n = int(n)
    except ValueError:
        sys.exit("Input Must be Integer")
    
    m = input("Enter M Number: ")
    try:
        m = int(m)
    except ValueError:
        sys.exit("Input Must be Integer")

    if m > n:
        pass
    else:
        # swap values
        n,m = m ,n
    
    res = fibonacci(m, n)
    if not res:
        print(res)

if __name__ == '__main__':
    main()
