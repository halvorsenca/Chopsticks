"""
Chopsticks.py
Program Three Implementation.
"""
from ChopsticksGame import ChopsticksGame
from aima.games import random_player
from aima.games import query_player
from aima.games import alphabeta_player, alphabeta_cutoff_search

__author__ = "Chris Campell, Cydney Caldwell, Chad Halvorsen"
__version__ = "10/2/2017"


def main(num_hands, num_fingers):
    """
    TODO: method header.
    :return:
    """
    # Initialize the game by creating an instance of the ChopsticksGame inherited from the Game class:
    chopsticks = ChopsticksGame(num_hands, num_fingers)
    # Play a game of Chopsticks against a human:
    chopsticks.play_game(random_player, query_player)

if __name__ == '__main__':
    main(num_hands=2, num_fingers=5)
