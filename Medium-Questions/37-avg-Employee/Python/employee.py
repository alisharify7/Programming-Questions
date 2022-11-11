import sys
from tabulate import tabulate

def get_int(msg):
    """Return only int input otherwise continue loop"""
    while True:
        n = input(msg).strip()
        try:
            n = int(n)
        except ValueError:
            continue
        else:
            return n

            
def get_pay(msg):
    """Return only pay number between 1-9 otherwise continue loop"""
    while True:
        n = input(msg).strip()
        try:
            n = int(n)
            if 0 < n < 10:
                return n
            else:
                continue
        except ValueError:
            continue
        else:
            return n

def get_sex(msg):
    """Return only sex type of employees [0 , 1] otherwise continue loop"""
    while True:
        n = input(msg).strip()
        if n in ["1", "0"]:
            return n
        else:
            continue

def get_employees():
    """
        this function take all employees
    """
    employees = []
    counter = 0
    while True:
        if counter != 0:
            flag = input("That's all the employees?  (YES,NO): ")
            if (flag.upper() in ["YES", "Y"]):
                return employees
        counter += 1
        name = input(f"Enter Employee {counter} Name: ").strip() 
        sex = get_sex(f"Enter Employee {counter} sex (1=man, 0=woman): ").strip()
        year = input(f"Enter Employee {counter} year: ").strip()
        pay = get_pay(f"Enter Employee {counter} pay: ")  
        
        employe = {
            "name": name,
            "sex":sex,
            "year":year,
            "pay":pay
        }
        employees.append(employe)


def find_eployee(data, flag):
    """
        this function take an searchable object and search into it 
        to seach for flag and return number of all flag
    """
    counter = 0
    for e in data:  
        if e["sex"] == flag:
            counter += 1
    return counter

def get_avg_pay(data, sex):
    """
        this function take and sex and search into data 
        and return average of pay for all employees with input sex
    """
    counter = 0
    pay = 0
    for e in data:  
        if e["sex"] == sex:
            counter += 1
            pay = e["pay"]
    
    return pay / counter


def main():
    employees = get_employees()
    # get numebr of employees
     
    n_woman = find_eployee(data=employees, flag="0")
    n_man = find_eployee(data=employees, flag="1")
    avg_woman_pay = get_avg_pay(employees, sex="0")
    avg_man_pay = get_avg_pay(employees, sex="1")
    all_employes = len(employees)
    table = [
        ["all employes", all_employes],
        ["number of womans", n_woman],
        ["number of mans", n_man],
        ["average of pay for womans", avg_woman_pay],
        ["average of pay for mans", avg_man_pay]
    ]
    print(tabulate(table, tablefmt="grid"))



if __name__ == '__main__':
    main()