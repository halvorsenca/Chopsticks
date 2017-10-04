"""
ChopsticksGame.py
A subclass of aima's Game class. A game is similar to a problem, but it has a utility for each state and a terminal
test instead of a path cost and a goal test.
"""
from aima.utils import *
from aima.games import Game
from aima.games import GameState
from copy import deepcopy

__author__ = "Chris Campell"
__version__ = "10/3/2017"


class ChopsticksGame(Game):
    """
    TODO: class header.
    """
    initial = None

    def __init__(self, num_hands=2, num_fingers=5):
        # self.initial = {'human': (1,1), 'cpu':(1,1), 'turn': 'h'}
        self.num_hands = num_hands
        self.num_fingers = num_fingers
        # Every move is possible starting out; takes the form (from_hand, to_opponents_hand) indexed L=0, R=1:
        moves = [(from_hand, to_hand) for from_hand in range(0, num_hands) for to_hand in range(0, num_hands)]
        human_hands = tuple(1 for i in range(num_hands))
        cpu_hands = tuple(1 for i in range(num_hands))
        self.initial = GameState(to_move='h', utility=0, board={'human': human_hands, 'cpu': cpu_hands}, moves=moves)

    def actions(self, state):
        """
        actions: Returns a list of allowable moves given the current state.
        :param state: The state of the game.
        :return possible_actions: A list of performable actions of the form (from_hand: L or R, to_hand: L or R).
        """
        return state.moves

    def calculate_utility(self, initial_state, resultant_state):
        """
        calculate_utility: Helper method for result, calculates the utility of a move given the state and desired
            move.
        :param initial_state: The initial gamestate.
        :param resultant_state: The resulting gamestate.
        :param move: The desired move.
        :return utility: The utility of the resultant gamestate.
        """
        """If 'X' wins with this move, return 1; if 'O' wins return -1; else return 0."""
        raise NotImplementedError

    def result(self, state, move):
        """
        result: Returns the state that results from making a move in the provided state.
        :param state: The initial state.
        :param move: The move performed in the initial state.
        :return resultant_state: The state resulting from the given move.
        """
        resultant_state = deepcopy(state)
        if state.to_move == 'h':
            # It is the human's turn to move:
            for from_hand, to_hand in move:
                resultant_state.board['cpu'][to_hand] = (resultant_state.board['cpu'][to_hand]
                                                         + (resultant_state.board['human'][from_hand] % 5))
        else:
            # It is the computer's turn to move:
            for from_hand, to_hand in move:
                resultant_state.board['human'][to_hand] += (resultant_state.board['human'][to_hand]
                                                            + (resultant_state.board['cpu'][from_hand] % 5))
        resultant_state.moves = self.actions(resultant_state)
        resultant_state.utility = self.calculate_utility(state, resultant_state)
        return resultant_state

    def utility(self, state, player):
        """
        utility: The value of the final state which is returned to the player.
        :param state:
        :param player:
        :return:
        """
        raise NotImplementedError

    def terminal_test(self, state):
        """
        terminal_test: Returns whether or not the provided state is a final state for the game.
        :param state:
        :return:
        """
        raise NotImplementedError

    def display(self, state):
        if isinstance(state, GameState):
            human_readable_moves = []
            for i, j in state.moves:
                from_hand = None
                to_hand = None
                if i == 0:
                    from_hand = 'L'
                else:
                    from_hand = 'R'
                if j == 0:
                    to_hand = 'L'
                else:
                    to_hand = 'R'
                human_readable_moves.append((from_hand, to_hand))
            game_state = 'to_move=%s, utility=%d, board=%s, moves of form (from_my, to_opponent)=%s' \
                         % (state.to_move, state.utility, state.board, human_readable_moves)
            print(game_state)
        else:
            super().display(state=state)
