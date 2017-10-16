"""
ChopsticksGamestate.py
"""


class ChopsticksGameState:
    to_move = None
    utility = None
    board = None
    moves = None
    last_move = None
    _hashed_value = None
    count = 0

    def __init__(self, to_move, utility, board, moves, last_move, count):
        self.to_move = to_move
        self.utility = utility
        self.board = board
        self.moves = moves
        self.last_move = last_move
        self.count = count

    def __hash__(self):
        if self._hashed_value is None:
            hashable_board = tuple((self.board['human'], self.board['cpu']))
            hashable_moves = tuple(move for move in self.moves)
            hashable_tuple = tuple((self.to_move, self.utility, hashable_board, hashable_moves, self.last_move))
            self._hashed_value = hash(hashable_tuple)
        return hash(self._hashed_value)

    def __eq__(self, other):
        if isinstance(other, ChopsticksGameState):
            if self._hashed_value is not None:
                if other._hashed_value is not None:
                    return self._hashed_value == other._hashed_value
                else:
                    return self._hashed_value == other.__hash__()
            else:
                if other._hashed_value is not None:
                    return self.__hash__() == other._hashed_value
                else:
                    return self.__hash__() == other.__hash__()
        else:
            return NotImplementedError

    def __repr__(self):
        game_repr = '(to_move=%s, utility=%d, board=%s, moves=%s, last_move=%s)' \
                     % (self.to_move, self.utility, self.board, self.moves, self.last_move)
        return game_repr

