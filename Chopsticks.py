"""
Chopsticks.py
Program Three Implementation.
"""
from ChopsticksGame import ChopsticksGame
from aima.games import random_player, query_player
from aima.games import alphabeta_player, alphabeta_cutoff_search
from aima.games import minimax_decision

__author__ = "Chris Campell, Cydney Caldwell, Chad Halvorsen"
__version__ = "10/2/2017"

def minimax_player(game, state):
    return minimax_decision(state=state, game=game)

def main(num_hands, num_fingers):
    """
    main: Plays the chopsticks game with the provided number of hands and fingers.
    :param num_hands: The number of hands the players have.
    :param num_fingers: The number of fingers the players have.
    :return:
    """
    # Initialize the game by creating an instance of the ChopsticksGame inherited from the Game class:
    chopsticks = ChopsticksGame(num_hands, num_fingers)
    # Play a game of Chopsticks against a human (cpu goes first):
    chopsticks.play_game(random_player, query_player)

if __name__ == '__main__':
    main(num_hands=2, num_fingers=5)
