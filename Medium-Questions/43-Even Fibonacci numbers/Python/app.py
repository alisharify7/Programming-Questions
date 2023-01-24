import os


def generate_fib(number):
    """
        this function get a number and return a
        sequence of fibonacci number to that number 
    """
    fib_sequence = []
    a = 0
    b = 1
    c = 0
    while True:
        c = a + b
        fib_sequence.append(c)
        a = b
        b = c
        if c >= number:
            return fib_sequence
    return fib_sequence


def main():
    f = generate_fib(4_000_000)
    f = [each for each in f if each % 2 == 0]
    print(sum(f))


if __name__ == '__main__':
    main()