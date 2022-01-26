#!/usr/bin/python3

# from games import games
import games

games_list = [
    {
        'name': 'Memory Game',
        'description': 'a sequence of numbers will appear for 1 '
                       'second and you have to guess it back',
        'class': games.memory_game.MemoryGame
    },
    {
        'name': 'Guess Game',
        'description': 'guess a number and see if you chose like the computer',
        'class': games.guess_game.GuessGame
    },
    {
        'name': 'Currency Game',
        'description': 'try and guess the value of a random amount of USD in NIS',
        'class': games.currency_roulette_game.CurrencyRouletteGame
    }
]
