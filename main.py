"""
Reinforcement Learning for TicTacToe

Usage:
    main.py --learn [--episodes=<num>] [--sparring=<partner>] [--agent=<name>]
    main.py --play [--opponent=<name>]

Options:
    -h --help               Show this screen
    --learn                 Train a new agent
    --play                  Play against an agent
    --algo=<choice>         Which RL algorithm to use
    --episodes=<num>        Number of episodes to use for training
    --sparring=<partner>    Bot against which the agent plays during the learning
    --agent=<name>          Name of the agent (file)
    --opponent=<name>       Name of the agent (file) against which to play
"""

import sys, pygame
import tkinter as tk
from docopt import docopt

cell = """                   
                   
                   """


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

    window.mainloop()

def training():
    pass



if __name__ == "__main__":
    print("Lets play a game...")
    
    arguments = docopt(__doc__)

    if arguments['play']:
        start_game()
    if arguments['learn']:
        training()