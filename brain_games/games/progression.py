import random

GAME_RULE = 'What number is missing in the progression?'


def get_content():
    progress_length = random.randint(5, 10)
    start = random.randint(1, 10)
    difference = random.randint(1, 10)
    progress = [str(start + difference * i) for i in range(progress_length)]
    hidden_index = random.randint(0, progress_length - 1)
    correct_answer = progress[hidden_index]
    progress[hidden_index] = '..'
    question = ' '.join(progress)

    return question, correct_answer
