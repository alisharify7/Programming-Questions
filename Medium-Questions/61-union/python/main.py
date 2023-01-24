import os, sys


def get_maqsom(n):
    maqsom = set()
    for i in range(1, n+1):
        if n % i == 0:
            maqsom.add(i)
    return maqsom


def main():
    n = input("Enter First Number: ")
    m = input("Enter Second Number: ")
    try:
        n = int(n)
        m = int(m)
    except ValueError:
        sys.exit("Input Must be Integer")

    n_maq = get_maqsom(n)
    m_maq = get_maqsom(m)
    
    
    # print union of between to sets
    print(n_maq & m_maq)




if __name__ == "__main__":
    main()