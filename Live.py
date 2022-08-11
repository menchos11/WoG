from tests import test_input
import GuessGame
import MemoryGame
import CurrencyRouletteGame


def welcome(name):
    print(f"hello", name, "and welcome to the World Of Games (WoG). \n"
                          "Here you can find many cool games to play.")
    return ""


def load_game():
    game = input("Please choose a game to play: "
                     "\n1. Memory Game - a sequence of numbers will appear for 1 second and you have to guess it back "
                     "\n2. Guess Game - guess a number and see if you chose like the computer "
                     "\n3. Currency Roulette - try and guess the value of a random amount of USD in ILS")
    game = test_input("1", "3", game)

    difficult = input("Please choose game difficulty from 1 to 5:")
    difficult = test_input("1", "5", difficult)

    if int(game) == 1:
        print("Memory Game - a sequence of numbers will appear for 1 second and you have to guess it back\n")
        MemoryGame.play(difficult)
    elif int(game) == 2:
        print("Guess Game - guess a number and see if you chose like the computer\n")
        GuessGame.play(difficult)
    else:
        print("Currency Roulette - try and guess the value of a random amount of USD in ILS")
        CurrencyRouletteGame.play(difficult)

