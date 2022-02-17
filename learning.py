import random
import numpy as np
from bot import DummyBot
from tictactoe import TicTacToe, X_PLAYER, O_PLAYER

# TODO copy paste some standard RL algo


# TODO return either a q table, or a policy, or a unicorn
def q_learning(game, episodes, sparring, name, alpha, gamma):
    print("Q-Learning")

    is_first_player = True

    # we wamt to learn Q*(s,a)

    # what is the set of all states
    # in tic tac toe: 

    Q = np.zeros((self.game.state_space, self.game.action_space))

    # 1) init q table (randomly possible, but final states must be 0)

    # 2) loop for each episode

    for episode in range(episodes):

    # 3) init S (actually S should be always the same here)

        S = None
        s_init_oracel = random.random()

        if s_init_oracel > 0.5:
            sparring.make_move()
            is_first_player = False
        
        S = self.game.board

    while True:

        # 4) choose A from policy derived by Q (epsilon)


        nth_state = self.game.get_num_of_state(S)

        action_list = Q[nth_state, :]

        # TODO not all actions are actually admissible, mark invalid actions with a -1

        max_action = np.argmax(action_list)

        move = self.game.selected_action_to_move(max_action)

        # 5) take action, and obserse s' and r
        
        _, reward = self.game.set_cell(is_first_player, O_PLAYER, move[0], move[1])

        # 6) update Q with equation

        new_S = self.game.board
        new_nth_state = self.game-get_num_of_state(new_S)
        new_action_list = Q[new_nth_state, :]
        new_max_action = np.argmax(new_action_list)
        
        # NOTE this is the bellman equation (more or less)
        Q[nth_state, max_action] = Q[nth_state, max_action] + alpha * (reward + gamma * (Q[new_nth_state, new_max_action] - Q[nth_state, max_action]))

        # 7) move to new state
        # NOTE: this happens automatically within the class TicTacToe

        # 8) do until fnal state is reached
        has_ended, _ = self.game.check_game()

        if has_ended:
            break


# TODO mc is also okay... either one is enough
def mc_learning(episodes, sparring, name):
    print("Monte Carlo-Learning")
    pass