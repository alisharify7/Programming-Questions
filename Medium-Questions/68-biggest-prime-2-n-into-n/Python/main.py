import os,sys



def is_prime(n):
    """
        this function take an number and
        check number is prime number or not
    """
    for each in range(2,n):
        if n % each == 0:
            return False
    return True



def get_prime_factor(n):
    """
        this function take an number
        and factors of that number
    """
    maqsom = []
    for i in range(2, int(round(n / 2)+ 1)):
        if n % i == 0:
            maqsom.append(i)
    maqsom = [x for x in maqsom if is_prime(x)]
    
    return maqsom



def main():
    number = int(input("Enter a Number: "))

    biggest = 0
    big_n = 0

    # iterate over 1 to n
    for each in range(2, number + 1):

        # get each number factors
        n_maq = get_prime_factor(each)
        
        # print factor of each number 
        print(f"{each}: {n_maq}")
        
        if len(n_maq) >= biggest:
            big_n = each
            biggest = len(n_maq)

    print(f"Number {big_n} with {biggest} prime factor")


if __name__ == "__main__":
    main()
