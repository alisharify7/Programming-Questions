import sys


def get_int(message):
    """
        This function get input from user
        ONLY int input
    """

    n = input(message).split(',')
    numbers = []
    for each in n:
        try:
             each =int(each)     
        except ValueError:
             print("Invalid format Number")
             sys.exit(1)
        else:
             numbers.append(each)
    return numbers


def is_perfect(number):
    maqsom = []
    for i in range(1,number):
        if number % i == 0:
             maqsom.append(i)
    total = 0
    for each in maqsom:
        total+= each
    if total == number:
        return True
    return False

def main():
    print("""
    Enter list of Number
        in format of =>   1,2,3,4,5,6
    """)
    n = get_int("prompt: ")
    for i in n:
         
         if is_perfect(i):
              print(f"{i} is perfect number")
              n = input("Do you wanna continue? [y,n]: ")
              if n.upper() in ["N", "NO"]:
                   sys.exit("Exit !")

         if not is_perfect(i):
              print(f"{i} is not perfect number")
              n = input("Do you wanna continue? [y,n]: ")
              if n.upper() in ["N", "NO"]:
                   sys.exit("Exit !")
        





if __name__ == '__main__':
        main()