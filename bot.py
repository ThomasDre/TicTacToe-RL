from tictactoe import TicTacToe, X_PLAYER, O_PLAYER
import random

class DummyBot {

    def __init__(self, game):
        self.game = game
        self.is_first = None

    def make_move(self):
        possible_moves = self.game.possible_moves()

        choice = random.randint(0, len(possible_moves) - 1)
        move = possible_moves[choice]

        if self.is_first == None:
            self.is_first = True if self.game.started == False else False

        self.game.set_cell(self.is_first, X_PLAYER, move[0], move[1])
    
}