import sys
import random


options = ["rock", "paper", "sissors"]


def pic_random():
    """
       this function take a random option between rock-paper-sessors 
    """    
    op = random.choice(options)
    return op


def get_valid_option(msg):
    """
        this function only take valid input from user 
    """
    while True:
        n = input(msg).strip()
        if n in ["1", "2", "3"]:
            return options[int(n) - 1]
        else:
            print("invalid option Please select Between 1,2,3 ")
            continue


def main():
    user = 0
    bot = 0
    user_selected = []
    bot_selected = []

    for each in range(5):
        # get user input
        select_user = get_valid_option(f"Select Your {each + 1} option: ")
        user_selected.append(select_user)
        
        # get random option
        select_bot = pic_random()
        bot_selected.append(select_bot)

    for index,value in enumerate(user_selected):
        if value == bot_selected[index]:
            user +=1
            bot +=1
            continue

        if value == "rock" and bot_selected[index] != "paper":
            user += 1
            continue
        if value == "sissors" and bot_selected[index] != "rock":
            user += 1
            continue
        if value == "paper" and bot_selected[index] != "sissors":
            user += 1
            continue
        bot += 1

    

    print(f"bot: {bot} | you: {user}")
    for index, value in enumerate(user_selected):
        print(f"You: {value} Bot={bot_selected[index]}")
    
    if bot > user:
        print ("\t\t\t\tBot win !")
    elif bot < user:
        print ("\t\t\t\tYou win !")
    else:
        print ("\t\t\t\tgame Tie !")



if __name__ == '__main__':
    main()