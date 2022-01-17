#!/usr/bin python3

from Live import load_game, welcome


def main():
    print(welcome('Name'))
    game = load_game()
    if game.play():
        print("Great! You did it.")
    else:
        print("Too bad, better luck next time.")

    # game = MemoryGame(difficulty)
    # game.play()


if __name__ == "__main__":
    main()
