import os


def getBaseTriangle(size) -> list:
    n = [None] * size
    
    if len(n) >= 3:
        n[0] = 1
        n[-1] = 1

    if len(n) == 1:
        n[0] = 1

    elif len(n) == 2:
        n[0], n[1] = 1, 1

    return n



def makeThisLevel(plevel, l):
    global data
    def calculate_before_stage(s,e):
        response = []
        innerlist = data[s:n]

        is_sum = True
        value = None
        
        for index, value in enumerate(innerlist):
            try:
                v = (value + each[index+1])
                response.append(v)
            except IndexError:
                continue
        return response 


    
    if plevel <= 1:
        print("retrun it self")
        return l
    
    p = data[plevel]
    middle = len(p) // 2
    

    return None




def main():
    global data
    data = []

    x = int(input("level: "))
    plevel = 0
    for each in range(1, x+1):
        n = (getBaseTriangle(each))
        n = makeThisLevel(plevel, n)
        data.append(n)
        plevel += 1

    print(data)




if __name__ == "__main__":
    main()