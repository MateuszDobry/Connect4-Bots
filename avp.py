from exceptions import GameplayException
from connect4 import Connect4
from randomagent import RandomAgent
from MinMaxHeuristic import MinMaxHeuristicAgent
from MinMaxAgent import MinMaxAgent
from AlphaBetaAgent import AlphaBetaAgent
import sys 

connect4 = Connect4(width=7, height=6)
agent = AlphaBetaAgent('x')

while not connect4.game_over:
    connect4.draw()
    try:
        if connect4.who_moves == agent.my_token:
            n_column = agent.decide(connect4)
        else:
            while True:
                try:
                    n_column = int(input('enter column number (0-6): '))
                    if n_column < 0 or n_column >= connect4.width:
                        raise ValueError("Column number must be in the range 0-6.")
                    break
                except ValueError as e:
                    print(e)
                    print('Try again.')
        connect4.drop_token(n_column)
    except KeyboardInterrupt:
        print('\nThe game has been interrupted.')
        sys.exit()  
    except GameplayException:
        print('Invalid move.')

connect4.draw()
sys.exit()  
