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
    # Display the initial gamestate:
    # chopsticks.display(chopsticks.initial)
    # Create a random player:
    random_agent = random_player(game=chopsticks, state=chopsticks.initial)
    # Create a human player:
    human_agent = query_player(game=chopsticks, state=chopsticks.initial)
    # Play a game of Chopsticks:
    chopsticks.play_game(random_agent, human_agent)

if __name__ == '__main__':
    # TODO: Perform any declarations of project relative file paths, etc..
    main(num_hands=2, num_fingers=5)
