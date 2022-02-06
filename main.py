#!/usr/bin/python3

from Live import load_game, welcome
import main_scores
import score


def main():
    print(welcome('player'))
    choice = 'Y'
    while choice.lower() == 'y':
        game, difficulty = load_game()
        if game.play():
            score.add_score(difficulty)
            print("Great! You did it.")
        else:
            print("Too bad, better luck next time.")
        choice = input('Do you wish to continue? (y/N) ')
        while choice.lower() not in ('y', 'n'):
            choice = input("Invalid input, answer with 'y' or 'n' only")
    print("Goodbye!")


if __name__ == "__main__":
    main()
