#!/usr/bin/python3

from random import randint


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


