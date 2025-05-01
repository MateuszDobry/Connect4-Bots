from connect4 import Connect4
import copy

class AlphaBetaAgent:
    def __init__(self, token: str, depth: int = 5):
        self.my_token = token
        self.depth = depth

    def decide(self, connect4: Connect4,):
        for n_column in connect4.possible_drops():
            new_connect4 = copy.deepcopy(connect4)
            new_connect4.drop_token(n_column)
            if new_connect4.game_over and new_connect4.wins == self.my_token:
                return n_column
        alfa = -float('inf')
        v = -float('inf') # best value
        y = None # best move
        for n_column in connect4.possible_drops():
            new_connect4 = copy.deepcopy(connect4)
            new_connect4.drop_token(n_column)
            var = self.alphabeta(new_connect4, self.depth-1, False, alfa)
            if var > v:
                v = var
                y = n_column
        return y

    def alphabeta(self, connect4: Connect4, depth: int, maximizing: bool ,alpha: float = -float('inf'), beta: float = float('inf')):
        if connect4.game_over:
            if connect4.wins == self.my_token:
                return 1
            elif connect4.wins is None:
                return 0
            else:
                return -1
        if depth == 0:
            return self.heuristic(connect4)

        if maximizing:
            v = -float('inf')
            for n_column in connect4.possible_drops():
                new_connect4 = copy.deepcopy(connect4)
                new_connect4.drop_token(n_column)
                v = max(v, self.alphabeta(new_connect4, depth - 1, not maximizing, alpha, beta))

                alpha = max(alpha, v)
                if v >= beta:
                    break  # Beta cutoff
            return v
        else:
            v = float('inf')
            for n_column in connect4.possible_drops():
                new_connect4 = copy.deepcopy(connect4)
                new_connect4.drop_token(n_column)
                v = min(v, self.alphabeta(new_connect4, depth - 1, not maximizing, alpha, beta))

                beta = min(beta, v)
                if v <= alpha:
                    break  # Alpha cutoff
            return v


    def heuristic(self, connect4: Connect4):
            total = 0
            points = 0
            enemypoints = 0
            weights = [0, 5, 15, 50]  # Wagi dla 1, 2, 3 żetonów w czwórce

            for four in connect4.iter_fours():
                total += 1
                count_ours = four.count(self.my_token)
                count_empty = four.count('_')
                count_enemy = 4 - count_ours - count_empty

                points += weights[count_ours]
                enemypoints += weights[count_enemy]

            # zwraca wartosci od -1 do 1
            return (points - enemypoints) / (total * weights[-1])