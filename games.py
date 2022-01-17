#!/usr/bin python3

from random import randint
from time import sleep
import click
from currency_converter import CurrencyConverter


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


class GuessGame:
    def __init__(self, difficulty):
        self.difficulty = int(difficulty)

    @staticmethod
    def generate_number(start=1, end=101):
        return randint(start, end)

    @staticmethod
    def get_guess_from_user() -> str:
        return input("Enter your guess: ")

    def compare_results(self, guess) -> bool:
        return guess.isnumeric() and self.secret_number == int(guess)

    def play(self) -> bool:
        self.secret_number = self.generate_number(end=self.difficulty)
        return self.compare_results(self.get_guess_from_user())


class CurrencyRouletteGame:
    def __init__(self, difficulty):
        self.difficulty = int(difficulty)

    @staticmethod
    def get_money_interval(random_num, difficulty) -> (float, float):
        exact_value = CurrencyConverter().convert(random_num, 'USD', 'ILS')
        print(exact_value)
        return exact_value - (5 - difficulty), exact_value + (5 - difficulty)

    def get_guess_from_user(self, random_num) -> str:
        print(f"You need to guess how much {random_num} USD are in ILS")
        return GuessGame.get_guess_from_user()

    def play(self) -> bool:
        random_number = GuessGame.generate_number()
        minimum, maximum = self.get_money_interval(random_number, self.difficulty)
        print(minimum, maximum)
        user_guess = self.get_guess_from_user(random_number)
        return user_guess.isnumeric() and minimum <= float(user_guess) < maximum
