import random

GAME_RULE = 'Answer "yes" if the number is even, otherwise answer "no".'


def get_content():
    question = random.randint(0, 100)

    if question % 2 == 0:
        correct_answer = 'yes'
    else:
        correct_answer = 'no'

    return question, correct_answer
