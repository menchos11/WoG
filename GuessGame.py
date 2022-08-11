import random
from tests import test_input


def generate_number(difficulty):
    try:
        secret_number = random.randrange(1, int(difficulty), 1)
    except ValueError:
        secret_number = 1
    return secret_number


def get_guess_from_user(difficulty):
    guess_number = input("please enter a number in rane 1 - " + difficulty)
    guess_number = test_input("1", difficulty, guess_number)
    return guess_number


def compare_results(secret_number, guess_number):
    answer = 0
    if secret_number == guess_number:
        answer = 1
    return answer


def play(difficulty):
    secret_number = generate_number(difficulty)
    guess_number = get_guess_from_user(difficulty)
    compare = compare_results(secret_number, int(guess_number))
    if compare == 1:
        print("True")
    else:
        print("False")
