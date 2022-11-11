import sys



def get_percentage(p, value):
    """
        this function take a percentage and value and
        calculate the percentage of the value
    """
    return p * value / 100



def get_int(msg):
    """Return only int input otherwise continue loop"""
    while True:
        n = input(msg).strip()
        try:
            n = float(n)
        except ValueError:
            continue
        else:
            return n


def main():
    price = get_int("Enter Car Price: ")
    
    for year in range(10):
        per = get_percentage(20, price)
        price -= per
        print(f"in year {year + 1} car price is {price}")


if __name__ == '__main__':
    main()