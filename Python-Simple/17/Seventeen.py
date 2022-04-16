import sys


def find_seq(dna,sample):
    """return number of sequences OF sample in a dna"""
    point = 0
    for i in range(len(dna)):
        if (dna[i] == sample):
            point += 1
    return point        



def main():
    user = input("Enter Dna SEQUENCE: ").strip()
    lenght = len(user)

    biggest = 0
    for i in range(lenght):
        temp = find_seq(sample = user[i],dna = user)
        
        if (temp > biggest):
            biggest = temp

    # print biggest number  of sequences in dna
    print(biggest)        
    














main()