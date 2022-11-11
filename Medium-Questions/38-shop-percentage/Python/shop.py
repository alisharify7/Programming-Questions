import sys


def get_int(msg):
    while True:
        n = input(msg).strip()
        try:
            n = int(n)
        except ValueError:
            continue
        else:
            return n

def get_product():
    """
        this function take and product information and return in 
        format of dict {}
    """
    while True:
        price = get_int("Enter Product price: ")
        degree = get_int("Enter Product degree: ")
        if degree in [1,2,3,4]:
            return {"price" : price, "degree": degree} 
        else:
            print("Invalid input. try again")
            continue

def process_procuts(info):
    """
        this function calculate seller percentage of this product
    """
    if info["degree"] == 1:
        if info["price"] <= 1_000_000:
            return  6 * info["price"] / 100
        elif 1_000_000 < info["price"] > 2_000_000:
            return  7 * info["price"] / 100
        else:
            return  10 * info["price"] / 100

    if info["degree"] == 2:
        if info["price"] < 1_00_000:
            return  4 * info["price"] / 100
        else:
            return  6 * info["price"] / 100
    if info["degree"] == 3:
        return  41.2 * info["price"] / 100
    if info["degree"] == 4:
        return  5 * info["price"] / 100


def main():
    procuts_info = get_product()
    seller = process_procuts(procuts_info)

    print(f"Seller percentage is ${seller} of ${procuts_info['price']} ")


if __name__ == '__main__':
    main()