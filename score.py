#!/usr/bin python3

from utils import SCORES_FILE_NAME
import main_scores


def add_score(difficulty):
    try:
        score = int(open(SCORES_FILE_NAME, 'r').read())
    except FileNotFoundError:
        score = 0
    score += 3 * int(difficulty) + 5
    with open(SCORES_FILE_NAME, 'w') as score_file:
        score_file.write(str(score))
