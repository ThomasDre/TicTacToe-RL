"""
Reinforcement Learning for TicTacToe

Usage:
    main.py --learn [--episodes=<num>] [--sparring=<partner>] [--agent=<name>] [--q | --mc]
    main.py --play [--opponent=<name>]

Options:
    -h --help               Show this screen
    --learn                 Train a new agent
    --play                  Play against an agent
    --q                     Use Q-Learning
    --mc                    Use Monte-Carlo
    --episodes=<num>        Number of episodes to use for training
    --sparring=<partner>    Bot against which the agent plays during the learning
    --agent=<name>          Name of the agent (file)
    --opponent=<name>       Name of the agent (file) against which to play
"""

import sys, pygame
import tkinter as tk
from docopt import docopt
import functools
from learning import q_learning, mc_learning
from tictactoe import TicTacToe, X_PLAYER, O_PLAYER
from bot import DummyBot

game = TicTacToe()

# Makes the cell big daddy size
cell = """                   
                   
                   """


# callback for the 9 tic tac toe fields
def cell_clicked(event, param):
    x = param[0]
    y = param[1]

    dummy = True if game.active_player == 'X' else False

    status = game.set_cell(dummy, X_PLAYER, x, y)
    print(game.board)
    print(game.check_game())
    print(status)


def start_game():
    # pygame.init()
    # size = width, heigth = 500, 400
    # screen = pygame.display.set_mode(size)
    # while 1:
    #     1 + 1

    window = tk.Tk()

    window.geometry("300x300")

    box_size_width = 250
    box_size_height= 25

    for i in range(3):
        for j in range(3):
            frame = tk.Frame(
                master=window,
                relief=tk.RAISED,
                borderwidth=1,
                width=box_size_width
            )
            frame.grid(row=i,column=j)
            label = tk.Label(master=frame, text=cell)
            label.pack()
            label.bind('<Button-1>', functools.partial(cell_clicked, param=(i,j)))
    

    window.mainloop()



if __name__ == "__main__":
    print("Lets play a game...")
    
    arguments = docopt(__doc__)

    if arguments['--play']:
        start_game()
    if arguments['--learn']:
        episodes = 10000
        # TODO Implement A Bot
        sparring_partner = DummyBot()
        # TODO Use this name, to be able to save different agents
        name = 'DUMMY AGENT NAME'
        algorithm = q_learning

        # set non default parameters
        if arguments['--episodes']:
            episodes = int(arguments['--episodes'])
        if arguments['--agent']:
            name = arguments['--agent']
        if arguments['--mc']:
            algorithm = mc_learning

        algorithm(game, episodes, sparring_partner, name)
