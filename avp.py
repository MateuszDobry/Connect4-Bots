from exceptions import GameplayException
from connect4 import Connect4
from randomagent import RandomAgent
from MinMaxHeuristic import MinMaxHeuristicAgent
from MinMaxAgent import MinMaxAgent
from AlphaBetaAgent import AlphaBetaAgent
import sys

connect4 = Connect4(width=7, height=6)

# Here you can change the bot to the one you want to play with, and his token
agent = AlphaBetaAgent('x')

while not connect4.game_over:
    connect4.draw()
    try:
        if connect4.who_moves == agent.my_token:
            n_column = agent.decide(connect4)
        else:
            while True:
                user_input = input('Enter column number (0-6) or press "q" to quit: ')
                if user_input.lower() == 'q':
                    print('\nThe game has been interrupted.')
                    sys.exit()  # Zakończ program
                try:
                    n_column = int(user_input)
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
