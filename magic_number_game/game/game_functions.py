import os, random

PLAYER_NAME = None
MIN_NUMBER = 1
MAX_NUMBER = 10


def clear_screen():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

def intro():
    print("-"*50, "MAGIC NUMBERS", "-"*50)
    get_player_name()
    print(f"I have a number between {MIN_NUMBER} and {MAX_NUMBER}. Can you guess it?")

def get_player_name():
    global PLAYER_NAME

    response = input("What is your name? ")
    PLAYER_NAME = response

def get_player_number():
    return input("What is your number? ")

def game_loop():
    max_tries = 3
    print(f"You have {max_tries} tries.")
    magic_number = str( random.randint(MIN_NUMBER, MAX_NUMBER) )
    player_number = get_player_number()

    while player_number != magic_number:
        max_tries -=1
        if max_tries == 0:
            exit_game()
        
        print(f"Wrong guess. You have {max_tries} tries left.")
        player_number = get_player_number()

def exit_game():
    clear_screen()
    print("Sorry, you lost the game :(")
    exit()