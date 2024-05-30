

def main():
    x = input().strip()
    repetitions = dict()

    previewsWord = x[1:]
    previewsCounter = 0
    repetitions[previewsWord] = previewsCounter
    

    for currentWord in x:

        if previewsWord == currentWord: # same as previous word
            previewsCounter += 1 
            continue
        
        if previewsWord != currentWord: # new word in lit
            if repetitions[previewsWord] < previewsCounter: # check count of current word is grater than previous word counter 
                repetitions[previewsWord] = previewsCounter

            previewsWord = currentWord
            previewsCounter = 1
            if previewsWord in repetitions:
                if repetitions[previewsWord] < previewsCounter: # check count of current word is grater than previous word counter 
                    repetitions[previewsWord] = previewsCounter
            else:
                previewsCounter = 1
                repetitions[previewsWord] = previewsCounter
                
            continue

    if repetitions[previewsWord] < previewsCounter:
        repetitions[previewsWord] = previewsCounter

    repetitions = [int(each) for each in repetitions.values()]
    repetitions.sort(reverse=True)
    print(repetitions[0])


if __name__ == '__main__':
    main()
