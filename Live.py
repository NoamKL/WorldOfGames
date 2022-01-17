#!/usr/bin/python3

from settings import games_list


def welcome(name):
    return f'Hello {name} and welcome to the World of Games (WoG).' \
           f'\nHere you can find many cool games to play.\n'


def load_game():
    print('Please choose a game to play: ')
    for index, game in enumerate(games_list):
        print(f'{index+1}. {game["name"]} - {game["description"]}')
    # for index, (game_name, description) in enumerate(games_dict.items()):
    #     print(f'{index+1}. {game_name} - {description}')
    choice = input()

    while not choice.isnumeric() or int(choice) not in range(1, len(games_list)+1):
        choice = input('Invalid choice, please try again: ')

    difficulty = input('Please choose game difficulty from 1 to 5: ')
    while not difficulty.isnumeric() or int(difficulty) not in range(1, 6):
        difficulty = input('Invalid choice, please try again: ')

    # creates and returns the game object
    return games_list[int(choice)-1]["class"](difficulty)
