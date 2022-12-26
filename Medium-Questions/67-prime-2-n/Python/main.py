import os,sys


def get_factor(n):
    """
        this function take an number and factors of that number
    """
    maqsom = []
    for i in range(1, int(round(n / 2)+ 1)):
        if n % i == 0:
            maqsom.append(i)

    if 1 not in maqsom:
        maqsom.append(1)
    
    if n not in maqsom:
        maqsom.append(n)
    
    return maqsom


def main():
    number = int(input("Enter a Number: "))
    
    target_number = 0
    len_number = 0

    # iterate over 1 to n
    for each in range(1, number + 1):
        # get each number factors
        n_maq = get_factor(each)
        # print factor of each number 
        print(f"{each}: {n_maq}")

        # keep track of number that have biggest factors
        if len(n_maq) > len_number:
            target_number = each
            len_number = len(n_maq)
    

    # print rsuallt
    print(f"Number \33[32m{target_number}\33[0m have \33[32m{len_number}\33[0m factors")


if __name__ == "__main__":
    main()
