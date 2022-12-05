import os, sys


class number:
    """
        meta class for numbers
        in this class all methods available
    """
    def all_2digit_equal(self):
        print("\33[1m \33[32m --start of All 2 digit numbers that first number and second is qual \33[0m")
        for i in range(1,101):
            if len(str(i)) == 2:
                temp = str(i)
                if temp[0] == temp[1]:
                    print(i, end=" - ")
        print("")
        return("\33[1m \33[32m --End of start of All 2 digit numbers that first number and second is qual \33[0m")
    
    def all_3digit_middle_zero(self):
        print("\33[1m \33[32m --start of All 3 digit numbers that middle number is zero \33[0m")
        for i in range(100,1000):
            temp = str(i)
            if temp[1] == "0":
                print(i, end=" - ")
        print("")
        return("\33[1m \33[32m --End of All 3 digit numbers that middle number is zero \33[0m")
    
    def first_second_second(self):
        print("\33[1m \33[32m --start of All 3 digit numbers that sum of first number and second is less than third\33[0m")
        for i in range(100,1000):
            temp = str(i)
            if int(temp[1]) + int(temp[0]) < int(temp[2]):
                print(i, end=" - ")
        print("")
        return ("\33[1m \33[32m --End of  All 3 digit numbers that sum of first number and second is less than third \33[0m")

    def mirror_number(self):
        print("\33[1m \33[32m --start of All 4 digit numbers that each number is  mirror \33[0m")
        for i in range(1_000,10_000):
            temp = str(i)
            if temp[0] == temp[-1] and temp[1] == temp[-2]:
                print(i, end=" - ")
        print("")
        return ("\33[1m \33[32m --End of  All 4 digit numbers that each number is mirror\33[0m")



def main():
    n = number()
    print(n.all_2digit_equal())
    print(n.all_3digit_middle_zero())
    print(n.first_second_second())
    print(n.mirror_number())





if __name__ == '__main__':
    main()