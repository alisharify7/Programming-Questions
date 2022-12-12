import os, sys



def main():
    
    n = input("enter length of numbers: ")
    try:
        n = int(n)
    except ValueError:
        sys.exit("Input must be integer ")
    
    
    counter = 0
    numbers = []

    while n > counter:
        m = input(f"Enter Number {counter + 1}: ")
        try:
            m = int(m)
        except ValueError:
            print(" \33[33m invalid input \33[0m")
            continue
        else:
            numbers.append(m)
        counter +=1
    
    # sort numbers
    numbers.sort()
    
    # if length of input is even
    if len(numbers) % 2 == 0:
        # like [1, 2, 3, 4, 5, 6]
        #      [1, 2, <3, 4,> 5, 6] middle in this case in 3 and 4
        # we should get average of this two numbers For Median
        
        b, a = numbers[round(len(numbers) / 2) - 1], numbers[round(len(numbers) / 2)]  
        print(sum((a,b)) / 2)
    
    # if length if input is prime number
    # we just slice it to middele and round it to up
    # like [1, 2, 3,    <4>   5, 6, 7] in this case middle is 4
    # for getting 4 we should first get length of list and divided by 2
    # that give us 3.5 and we round it to up and we got 4
     
    elif len(numbers) % 2 != 0:
        # because in array we count from 0 we should increment 1 from result
        print(numbers[round(len(numbers) / 2) - 1])


if __name__ == "__main__":
    main()