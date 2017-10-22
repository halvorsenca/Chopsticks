"""
Chopsticks.py
Program Three Implementation.
"""
from ChopsticksGame import ChopsticksGame
from aima.games import random_player, query_player
import pandas as pd
from itertools import product

__author__ = "Chris Campell, Cydney Caldwell, Chad Halvorsen"
__version__ = "10/2/2017"


def main(num_hands, num_fingers):
    """
    main: Plays the chopsticks game with the provided number of hands and fingers.
    :param num_hands: The number of hands the players have.
    :param num_fingers: The number of fingers the players have.
    :return:
    """
    # Play a game of Chopsticks against a human (cpu goes first):
    num_players = 2
    state_action_table = {0: {'state': [], 'action': []}}
    num_states = num_fingers * num_hands * num_players
    output = []
    # Iterate over every possible state:
    for prod in product(range(num_fingers), repeat=6):
        human_hand_initial = tuple(list(prod)[0:3])
        cpu_hand_initial = tuple(list(prod)[3:])
        if human_hand_initial == (0, 0, 0) or cpu_hand_initial == (0, 0, 0):
            pass
        else:
            # Initialize the game by creating an instance of the ChopsticksGame inherited from the Game class:
            chopsticks = ChopsticksGame(num_hands, num_fingers, init_cpu_hands=cpu_hand_initial, init_human_hands=human_hand_initial)
            state = chopsticks.initial
            move = ChopsticksGame.minimax_player(chopsticks, state=state)
            # print("human_hand_init: %s, cpu_hand_init: %s, minimax_move: %s" % (human_hand_initial, cpu_hand_initial, move))
            parry_state = list(prod)
            # cpu = 0
            # human = 1
            parry_current_player = 0

            parry_tapper_tapped = [None, None]
            # human: 2,3,0,1
            # cpu: 0,1,2,3
            if move[0] == 0:
                parry_tapper_tapped[0] = 0
            if move[0] == 1:
                parry_tapper_tapped[0] = 1
            if move[1] == 0:
                parry_tapper_tapped[1] = 2
            if move[1] == 1:
                parry_tapper_tapped[1] = 3

            parry_string = format("%d %d %d %d %d %d %s,%s %s" % (list(prod)[0], list(prod)[1], list(prod)[2], list(prod)[3], list(prod)[4], list(prod)[5], parry_current_player, parry_tapper_tapped[0], parry_tapper_tapped[1]))
            output.append(parry_string)
            # print("parry_string: %d %d %d %d %s,%s %s" % (list(prod)[0], list(prod)[1], list(prod)[2], list(prod)[3], parry_current_player, move[0], move[1]))
    df_submit = pd.DataFrame(data=output)
    with open('submit_cpu_three_fingers.csv', 'w') as fp:
        df_submit.to_csv(fp,index=False)

if __name__ == '__main__':
    main(num_hands=3, num_fingers=5)
