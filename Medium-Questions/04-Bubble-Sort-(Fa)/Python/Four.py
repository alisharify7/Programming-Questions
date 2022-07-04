import sys


# linear function 
def linear_sort(list_tmp):
    """this function take a list and sort all of element in it, and return sorted list"""
    flag = 0
    lenght =len(list_tmp)

    while (flag <= lenght * lenght):
        for i in range(len(list_tmp) - 1):
            if (list_tmp[i] > list_tmp[i + 1]):
                tmp = list_tmp[i]
                list_tmp[i] = list_tmp[i + 1]
                list_tmp[i + 1] = tmp
            flag += 1
    return list_tmp


# unsorted lis with numbers
numbers = [102,1567,234,123,4,21,3,567,213,56,8,5]
final = linear_sort(numbers)
print(final)

sys.exit(0)