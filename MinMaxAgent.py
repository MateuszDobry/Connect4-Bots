from connect4 import Connect4
import copy


class MinMaxAgent:
    def __init__(self, token: str, depth: int = 5):
        self.my_token = token
        self.depth = depth

    def decide(self, connect4):
        for n_column in connect4.possible_drops():
            new_connect4 = copy.deepcopy(connect4)
            new_connect4.drop_token(n_column)
            if new_connect4.game_over and new_connect4.wins == self.my_token:
                return n_column  # Natychmiast wybieramy wygraną

        # Jeśli nie ma natychmiastowej wygranej, używamy Minimax
        v = -float('inf')
        y = None
        for n_column in connect4.possible_drops():
            new_connect4 = copy.deepcopy(connect4)
            new_connect4.drop_token(n_column)
            var = self.minimax(new_connect4, self.depth - 1, False)
            if var > v:
                v = var
                y = n_column
        return y

    def minimax(self, connect4: Connect4, depth: int, maximizing: bool):
        if connect4.game_over:
            if connect4.wins == self.my_token:
                return 1
            elif connect4.wins is None:
                return 0
            else:
                return -1

        if depth == 0:
            return 0

        if maximizing:
            v = -float('inf')
            for n_column in connect4.possible_drops():
                new_connect4 = copy.deepcopy(connect4)
                new_connect4.drop_token(n_column)
                v = max(v, self.minimax(new_connect4, depth - 1, not maximizing))
            return v
        else:
            v = float('inf')
            for n_column in connect4.possible_drops():
                new_connect4 = copy.deepcopy(connect4)
                new_connect4.drop_token(n_column)
                v = min(v, self.minimax(new_connect4, depth - 1, not maximizing))
            return v


