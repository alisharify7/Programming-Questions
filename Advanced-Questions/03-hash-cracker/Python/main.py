import csv
import hashlib



def hash_data(filename):
    with open(filename, 'r') as f:
        reader = csv.reader(f)
        reader.__next__()
        data = {}
        for row in reader:
            data[row[1].strip()] = 0

        return data


def main():
    filename = "../passwords.csv"
    hash_data_dict = hash_data(filename)

    counter = 0
    let_data = len(hash_data_dict.items())

    for each in range(1, (99_999+1)):
        if let_data == counter:
            break

        hash = hashlib.md5(str(each).encode("UTF-8")).hexdigest()

        if hash in hash_data_dict:
            hash_data_dict[hash] = each
            counter += 1

    print("----" * 21, end="\n")
    for each in hash_data_dict:
        print(f"the orginal password for hash value \033[31m <{each}> \033[0m is \033[33m {hash_data_dict[each]} \033[0m")
    print("----" * 21, end="\n")


if __name__ == "__main__":
    main()