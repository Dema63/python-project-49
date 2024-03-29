import prompt

ROUNDS = 3


def greet_and_get_name():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f"Hello, {name}!")
    return name


def start_game(game):
    name = greet_and_get_name()
    print(game.GAME_RULE)
    current_round = 0
    while current_round < ROUNDS:
        question, right_answer = game.get_content()
        print(f'Question: {question}')
        answer = input('Your answer: ')
        if right_answer == answer:
            print('Correct!')
            current_round += 1
            if current_round == ROUNDS:
                print(f'Congratulations, {name}!')
        else:
            correct_answer = right_answer
            feedback_message = (
                f'"{answer}" is wrong answer ;(. '
                f'Correct answer was "{correct_answer}".'
            )
            print(feedback_message)
            print(f"Let's try again, {name}!")
            break
