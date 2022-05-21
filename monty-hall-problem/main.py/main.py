import random
print("Monty Hall Problem")

def spotDoor():
    #door1
    spotChosen = random.randint(0, 2)
    doors[0] = spots[spotChosen]
    spots.pop(spotChosen)
    #door2
    spotChosen = random.randint(0, 1)
    doors[1] = spots[spotChosen]
    spots.pop(spotChosen)
    #door3
    doors[2] = spots[0]
    spots.pop(0)


def userFirstChoice():
    print(doorsVisual)
    global selectedDoor
    #input-check
    while True:
        try:
            print("Which door would you like to open?")
            selectedDoor = int(input())
        except:
            print("Please enter an integer between 1 and 3")
            continue
        if selectedDoor >= 1 and selectedDoor <= 3:
            break
        else:
            print("Please enter an integer between 1 and 3")
            continue
    selectedDoor -= 1
#reveal the one of the goats


def reveal():
    global revealedDoor
    revealedDoor = random.randint(0, 2)
    while revealedDoor == selectedDoor or doors[revealedDoor] == "CAR":
        revealedDoor = random.randint(0, 2)
    global doorsVisual
    doorsVisual = doorsVisual.replace(
        ("|     " + str(revealedDoor+1) + "     |"), "|    GOAT   |")
    print(doorsVisual)
    print("There is a " + doors[revealedDoor] +
          " behind door number " + str(revealedDoor + 1))
    print("Would you like to switch? (y/n)")
    global switch
    switch = str(input())
    while switch != "y" and switch != "n":
        print("Please enter y for yes or n for no")
        switch = str(input())
    if switch == "y":
        switch = True
    else:
        switch = False


def switchingDoor(switch):
    if switch:
        global switchTo
        switchTo = random.randint(0, 2)
        while switchTo == revealedDoor or switchTo == selectedDoor:
            switchTo = random.randint(0, 2)
        print("There is a " + doors[switchTo] +
              " behind door number " + str(switchTo+1))
        global doorsVisual
        if doors[switchTo] == "CAR":
            doorsVisual = doorsVisual.replace(
                ("|     " + str(switchTo+1) + "     |"), "|    CAR    |")
            doorsVisual = doorsVisual.replace(
                ("|     " + str(selectedDoor+1) + "     |"), "|    GOAT   |")
            print(doorsVisual)
            print('')
            print("You Won!")
        else:
            doorsVisual = doorsVisual.replace(
                ("|     " + str(selectedDoor+1) + "     |"), "|    CAR    |")
            doorsVisual = doorsVisual.replace(
                ("|     " + str(switchTo+1) + "     |"), "|    GOAT   |")
            print(doorsVisual)
            print('')
            print("You Lost!")

#opens selected door while switching door == false


def openingDoor(switch):
    if not switch:
        global notOpened
        notOpened = random.randint(0, 2)
        while notOpened == revealedDoor or notOpened == selectedDoor:
            notOpened = random.randint(0, 2)
        print("There is a " + doors[selectedDoor] +
              " behind door number " + str(notOpened+1))
        global doorsVisual
        if doors[selectedDoor] == "CAR":
            doorsVisual = doorsVisual.replace(
                ("|     " + str(selectedDoor+1) + "     |"), "|    CAR    |")
            doorsVisual = doorsVisual.replace(
                ("|     " + str(notOpened+1) + "     |"), "|    GOAT   |")
            print(doorsVisual)
            print('')
            print("You Won!")
        else:
            doorsVisual = doorsVisual.replace(
                ("|     " + str(notOpened+1) + "     |"), "|    CAR    |")
            doorsVisual = doorsVisual.replace(
                ("|     " + str(selectedDoor+1) + "     |"), "|    GOAT   |")
            print(doorsVisual)
            print('')
            print("You Lost!")


#Game Loop
while True:
    #global vars
    spots = ["GOAT", "GOAT", "CAR"]
    doors = ["door1", "door2", "door3"]
    doorsVisual = """
    |-----------|   |-----------|   |-----------|
    |           |   |           |   |           |
    |           |   |           |   |           |
    |     1     |   |     2     |   |     3     |
    |           |   |           |   |           |
    |           |   |           |   |           |
    |-----------|   |-----------|   |-----------|
    """

    spotDoor()
    userFirstChoice()
    reveal()
    switchingDoor(switch)
    openingDoor(switch)
    print("Would you like to play again? (y/n)")
    again = input()
    while again != "y" and again != "n":
        print("Please enter y for yes and n for no")
        again = input()
    if again == "y":
        continue
    else:
        print("Thanks")
        break
