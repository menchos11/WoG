import random
from tests import test_input
import os
from time import sleep


def generate_sequence(difficulty):
    ran_numbers = {}
    for number in range(0, difficulty):
        ran_numbers[number] = random.randrange(1, 101, 1)
    print(ran_numbers)
    sleep(0.7)
    os.system('cls')
    return ran_numbers


def get_list_from_user(difficulty):
    usr_numbers = {}
    for number in range(0, difficulty):
        try:
            usr_numbers[number] = int(input("please enter a number in rane 1 - 101:"))
        except ValueError:
            usr_numbers[number] = input("please enter a number")
        usr_numbers[number] = test_input("1", "101", usr_numbers[number])
    return usr_numbers


def is_list_equal(ran_numbers, usr_numbers):
    answer = "0"
    if ran_numbers == usr_numbers:
        answer = True
    else:
        answer = False
    return answer


def play(difficulty):
    ran_numbers = generate_sequence(difficulty)
    usr_numbers = get_list_from_user(difficulty)
    answer = is_list_equal(ran_numbers, usr_numbers)
    print(answer)
