import os, sys
from tabulate import tabulate

# each pules => 46
# 4% tax for all call's
# 23-8 am 50% 
# day 7 call is 75% off

def get_time(m):
    """ 
        this function get time by defination role
        0 - 23
    """
    while True:
        x = input(m)
        try:
            x = int(x)
            # for getting vlaid time  
            if 0 <= x <= 23:
                pass
            else:
                continue
        except ValueError:
            continue
        else:
            return x


def get_int(m):
    """ this function only accept numbers ! """
    while True:
        x = input(m)
        try:
            x = int(x)
        except ValueError:
            continue
        else:
            return x


def get_day(m):
    """ this function only accept number that between 0 -7 day of the week  """
    while True:
        x = input(m)
        try:
            x = int(x)
            
            if  0 <= x <= 7:
                return x
            else:
                continue

        except ValueError:
            continue
        else:
            return x


def gete_users():
    """ this function take users and replace them in structure like json response  """
    x = input("Enter Number Of Users: ")
    try:
        x = int(x)
    except ValueError:
        sys.exit("Invalid input :( ")
    
    users = []
    for i in range(x):
        temp = {}
        temp["user"] = i + 1
        temp["time"] = get_time(f"Enter Start Time of Call for User-{i + 1}: ")
        temp["pules"] = get_int(f"Enter Number of Pules for User-{i + 1}: ")
        temp["day"] = get_day(f"Enter Day of that User-{i + 1} Call: ")
        temp["price"] = 0
        users.append(temp)

    return users



def calculate_price(users):
    """ this function calculate price of each call """    
    for each in users:
        # check time and date
        each["price"] = (each["pules"] * 46)
        
        if each["time"] == 7:
            # 75 off
            each["price"] = each["price"] - (75 * (each["pules"] / 100)) 
        
        # check time fo 23 to 8
        if 0 <= each["time"] <= 8:
            each["price"] = each["price"] - (50  * each["price"] / 100  )

        # calculate tax -> 4 %
        each["price"] = each["price"] + (4 * each["price"] / 100)

    return users


def main():
    users = gete_users()
    prices = calculate_price(users)
    users = [ [each["user"] , each["time"] , each["pules"], each["day"], each["price"] ] for each in users]
    print(tabulate(users,headers=["user","time", "pules", "day", "price"], tablefmt="github"))


if __name__ == "__main__":
    main()
