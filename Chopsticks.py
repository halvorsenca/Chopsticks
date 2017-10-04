"""
Chopsticks.py
Program Three Implementation.
"""
from ChopsticksGame import ChopsticksGame

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
    chopsticks.display(chopsticks.initial)


if __name__ == '__main__':
    # TODO: Perform any declarations of project relative file paths, etc..
    main(num_hands=2, num_fingers=5)
