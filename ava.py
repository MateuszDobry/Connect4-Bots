import sys

from exceptions import GameplayException
from connect4 import Connect4
from randomagent import RandomAgent
from MinMaxHeuristic import MinMaxHeuristicAgent
from MinMaxAgent import MinMaxAgent
from AlphaBetaAgent import AlphaBetaAgent



connect4 = Connect4(width=7, height=6)

# Here you can change the bots to the ones you want to play , and their tokens
agent1 = AlphaBetaAgent('x')
agent2 = MinMaxHeuristicAgent('o')

if agent1.my_token == agent2.my_token:
    print('\nBots must have different tokens.')
    sys.exit()
while not connect4.game_over:
    connect4.draw()
    try:
        try:
            if connect4.who_moves == agent1.my_token:
                n_column = agent1.decide(connect4)
            else:
                n_column = agent2.decide(connect4)
            connect4.drop_token(n_column)
        except (ValueError, GameplayException):
            print('invalid move')
    except KeyboardInterrupt:
        print('\nThe game has been interrupted.')
        sys.exit()

connect4.draw()
