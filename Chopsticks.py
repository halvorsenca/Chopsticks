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
    initial_state = None
    goal_state = None

    def __init__(self, initial_state, goal_state):
        super().__init__(initial=initial_state, goal=goal_state)
        # TODO: Add additional parameters to __init__ as needed.

    def actions(self, state):
        """
        actions: TODO: method header.
        :param state:
        :return:
        """
        # TODO: Method body.
        pass

    def result(self, state, action):
        """
        result: TODO: method header.
        :param state:
        :param action:
        :return:
        """
        # TODO: Method body.
        pass

    def goal_test(self, state):
        """
        goal_test: TODO: method header.
        :param state:
        :return:
        """
        # TODO: Method body.
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
        # TODO: Method body.
        pass


class ChopsticksNode(Node):
    """
    ChopsticksNode: TODO: class header.
    """
    # TODO: Override parent class functionality (if needed).
    # TODO: Method body.
    pass


def a_star_search(problem, heuristic=None):
    """
    TODO: Method header.
    :param problem:
    :param heuristic:
    :return:
    """
    # TODO: method body.
    solution = None
    num_nodes_expanded = 0
    return solution, num_nodes_expanded


def main(num_hands, num_fingers, search_type):
    """
    TODO: method header.
    :return:
    """
    # Define our initial state to be a dictionary:
    initial_state = {'human': (1,1), 'cpu': (1, 1), 'turn': 'h'}
    # Define our desired goal state to be a human victory:
    desired_goal_state = {'human': (0, 0)}
    # Define an instance of the problem:
    problem = ChopsticksProblem(initial_state=initial_state, goal_state=desired_goal_state)
    # Solve the problem:
    solution = None
    if search_type is a_star_search:
        # heuristic = some_heuristic
        solution, num_nodes_expanded = a_star_search(problem=problem)
    if solution is not None:
        print("Solution: %s" % solution)
    else:
        print("No Solution Available.")


if __name__ == '__main__':
    # TODO: Perform any declarations of project relative file paths, etc..
    main(num_hands=2, num_fingers=5, search_type=a_star_search)
