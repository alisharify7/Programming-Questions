import os


def get_int(message):
    """
        This function get input from user
        ONLY int input
    """

    while True:
        n = input(message)
        try:
            n = int(n)
            return n
        except ValueError:
            continue

def get_student(round):
     """
        this function take students name and grade 
        and return in form of dict object
     """

     n = input(f"Enter student #{round + 1}# name ? ")
     g = input(f"Enter student #{round + 1}# Grade ? ")

     return {"name":n, "grade":g}
    
     

def remove_biggest(data):
    """
        this function remove student with biggest Grade
        from list and return list
    """
    first = 0
    deleted = 0    
    for each in enumerate(data):
         temp = int(each[1]["grade"])
         if temp >= first:
              first = temp
              deleted = each[0]
    
    del data[deleted]
    return data



def find_biggest(data):
    """
        this function find student with biggest grade
        and return it 
    """
    first = 0
    biggest = 0
    for each in data:
         temp = int(each["grade"])
         if temp >= first:
              first = temp
              biggest = each
    return biggest

def main():
    # get number of student from user
    n_student = get_int("Enter students Number: ")

    total = []
    # get all student and store it in total list
    for i in range(n_student):
        temp = get_student(i)
        total.append(temp)

    # remove student with biggest grade 
    total = remove_biggest(total)
    # find student with  biggest grade {second} - because we remove first one 
    second = find_biggest(total)
    
    
    print(f"{second['name']} is Second student in class with Grade {second['grade']}")


if __name__ == '__main__':
        main()



