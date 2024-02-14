import random

GAME_RULE = 'What number is missing in the progression?'


def generate_progression():
    progress_length = random.randint(5, 10)
    start = random.randint(1, 10)
    difference = random.randint(1, 10)
    progression = [str(start + difference * i) for i in range(progress_length)]
    return progression


def get_content():
    progression = generate_progression()
    hidden_index = random.randint(0, len(progression) - 1)
    correct_answer = progression[hidden_index]
    progression[hidden_index] = '..'
    question = ' '.join(progression)
    return question, correct_answer
