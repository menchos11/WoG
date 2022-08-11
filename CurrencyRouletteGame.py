from tests import test_input
import random
from currency_converter import CurrencyConverter


def get_money_interval(d, t):
    low_interval = int(t) - (5 - int(d))
    high_interval = int(t) + (5 - int(d))
    return low_interval, high_interval


def get_guess_from_user(usd):
    guess = (input("guess the currency of " + str(usd) + " in ils ="))
    guess = test_input("1", "999", guess)
    return guess


def play(difficulty):
    usd = random.randrange(1, 100, 1)
    c = CurrencyConverter()
    total_value_of_money = c.convert(usd, 'USD', 'ILS')
    interval = get_money_interval(difficulty, total_value_of_money)
    guess = get_guess_from_user(usd)
    if int(interval[0]) <= int(guess) <= int(interval[1]):
        print(True)
    else:
        print(False)
