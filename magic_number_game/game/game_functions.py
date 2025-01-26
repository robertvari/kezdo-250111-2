import os

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


def get_player_name():
    global PLAYER_NAME
    
    response = input("What is your name? ")
    PLAYER_NAME = response

def get_player_number():
    pass

def game_loop():
    pass

def exit_game():
    pass