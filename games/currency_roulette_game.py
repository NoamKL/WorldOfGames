#!/usr/bin/python3

from currency_converter import CurrencyConverter

from guess_game import GuessGame


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
