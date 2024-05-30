import os


def get_int():
    while True:
        x = input()
        try:
            x = int(x)
            return x
        except ValueError:
            continue


def get_str():
    while True:
        x = input()
        if x:
            return x
        continue


def main():
    key = get_str()
    length = get_int()
    words = []

    max_key_index = 0
    longest_key = None
    for i in range(length):
        w = get_str()
        if key in w:

            if w.index(key) > max_key_index:
                longest_key = w
                max_key_index = w.index(key)

            words.append(w)

    max_key_index += 1
    for each in words:
        if key in each:
            if each.index(key)+1 < max_key_index:
                gap = max_key_index - (each.index(key)+1)
                print(("*" * gap) + each)
            else:
                print(each)
        else:
            print(each)


if __name__ == '__main__':
    main()
