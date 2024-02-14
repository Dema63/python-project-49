import random
import operator

GAME_RULE = 'What is the result of the expression?'


def get_content():
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)

    operations = [('+', operator.add), ('-', operator.sub), ('*', operator.mul)]
    operation, func = random.choice(operations)
    question = f'{num1} {operation} {num2}'
    correct_answer = str(func(num1, num2))

    return question, correct_answer
