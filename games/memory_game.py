#!/usr/bin/python3

from time import sleep
import click

from guess_game import GuessGame


class MemoryGame:
    def __init__(self, difficulty):
        self.difficulty = int(difficulty)

    def generate_sequence(self) -> list:
        return [GuessGame.generate_number() for i in range(self.difficulty)]

    def get_list_from_user(self) -> list:
        print(f"Enter the numbers you have seen, separated by ENTER: ")
        return [input() for i in range(self.difficulty)]

    @staticmethod
    def is_list_equal(list1, list2) -> bool:
        try:
            # compare all corresponding integers in each list
            return all(map(lambda x, y: int(x) == int(y), list1, list2))
        except ValueError:  # if one of the lists contains non-numeric string
            return False

    def play(self) -> bool:
        random_list = self.generate_sequence()
        print(random_list)
        sleep(0.7)
        self.clear_screen()
        user_list = self.get_list_from_user()
        return self.is_list_equal(random_list, user_list)

    @staticmethod
    def clear_screen():
        # works only when run from CMD
        click.clear()
