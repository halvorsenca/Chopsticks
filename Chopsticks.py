"""
Chopsticks.py
Program Three Implementation.
"""

from aima.problem import Problem
from aima.node import Node

__author__ = "Chris Campell, Cydney Caldwell, Chad Halvorsen"
__version__ = "10/2/2017"


class ChopsticksProblem(Problem):
    """
    ChopsticksProblem
    TODO: Class header.
    """

    def __init__(self, initial_state, goal_state):
        super().__init__(initial=initial_state, goal=goal_state)
        # TODO: Add additional parameters to __init__ as needed.

    def actions(self, state):
        """
        actions: TODO: method header.
        :param state:
        :return:
        """
        pass

    def result(self, state, action):
        """
        result: TODO: method header.
        :param state:
        :param action:
        :return:
        """
        pass

    def goal_test(self, state):
        """
        goal_test: TODO: method header.
        :param state:
        :return:
        """
        pass

    def path_cost(self, c, state1, action, state2):
        """
        path_cost: TODO: method header.
        :param c:
        :param state1:
        :param action:
        :param state2:
        :return:
        """
        pass


class ChopsticksNode(Node):
    """
    ChopsticksNode: TODO: class header.
    """
    # TODO: Override parent class functionality (if needed).
    pass


def main():
    """
    TODO: method header.
    :return:
    """
    pass

if __name__ == '__main__':
    # TODO: Perform any declarations of project relative file paths, etc..
    main()

