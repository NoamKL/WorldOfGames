#!/usr/bin/python3

from Live import load_game, welcome

from score import add_score


def main():
    print(welcome('Name'))
    game, difficulty = load_game()
    if game.play():
        add_score(difficulty)
        print("Great! You did it.")
    else:
        print("Too bad, better luck next time.")


if __name__ == "__main__":
    main()
