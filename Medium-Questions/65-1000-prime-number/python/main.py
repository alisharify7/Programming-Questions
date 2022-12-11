import os, sys

# x ^ 34 - 9

def is_prime(n):
    for i in range(2, int(n / 2) +1):
        if n % i == 0 :
            return False
    return True

def main():
    primes = []
    for x in range(1, 1000):
        target = x ** 34 - 9
        temp = f"{x} ^34 - 9"
        if is_prime(target):
            primes.append(temp)
    print(primes)

if __name__ == "__main__":
    main()