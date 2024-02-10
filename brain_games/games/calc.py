import random

GAME_RULE = 'What is the result of the expression?'


def get_content():
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)

    operations = ['+', '-', '*']
    operation = random.choice(operations)

    question = f'{num1} {operation} {num2}'

    if operation == '+':
        correct_answer = str(num1 + num2)
    elif operation == '-':
        correct_answer = str(num1 - num2)
    elif operation == '*':
        correct_answer = str(num1 * num2)

    return question, correct_answer
