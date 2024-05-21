def main():
    x = int(input())
    songs = input().strip().split()
    
    previews_numbers = []
    timer = 0
    max_sequence = 0
    
    for each in songs:
        if max_sequence < timer:
            max_sequence = timer
        if each in previews_numbers:
            timer = 0
            previews_numbers = []
            previews_numbers.append(each)
            timer = 1
        else:
            timer += 1
            previews_numbers.append(each)
    else:
        if max_sequence < timer:
            max_sequence = timer

    print(max_sequence)    


# 2 3 4 5 2 10 9 8 6 1

        



if __name__ == '__main__':
    main()