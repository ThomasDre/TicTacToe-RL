import numpy as np

FIRST_PLAYER = 'X'
SECOND_PLAYER = '0'
EMPTY = '-'

class TicTacToe:
    def __init__(self):
        self.board = np.chararray((3,3))
        self.started = False
        self.active_player = FIRST_PLAYER

        self.board[:] = EMPTY

    def set_cell(self, is_first_player, x, y):
        """
        Makes a move if admissible
        """
        if is_first_player and self.active_player != FIRST_PLAYER:
            print("OOPS")
            return False

        if self.board[x,y].decode('utf-8') == EMPTY:
            sign = FIRST_PLAYER if is_first_player else SECOND_PLAYER
            self.board[x,y] = sign
            self.started = True

            self.active_player = SECOND_PLAYER if self.active_player == FIRST_PLAYER else FIRST_PLAYER

            return True
        else:
            return False

    def check_game(self):
        """
        Cheks whether the game ended, and who won or whether there was a draw
        Returns tuple of (hasEnded, status)

        where status == True means FIRST_PLAYER (X) won, status == False means SECOND_PLAYER (0) won, and status == None means there was a draw
        """
        for i in range(3):
            X_stack = []
            O_stack = []

            for j in range(3):
                print("TEST: " + self.board[i,j].decode('utf-8'))
                if self.board[i,j].decode('utf-8') == FIRST_PLAYER:
                    X_stack.append('c')
                if self.board[i,j].decode('utf-8') == SECOND_PLAYER:
                    O_stack.append('c')

            if len(X_stack) == 3:
                return True, True
            if len(O_stack) == 3:
                return True, False

            X_stack = []
            O_stack = []

            for j in range(3):
                if self.board[j,i].decode('utf-8') == FIRST_PLAYER:
                    X_stack.append('c')
                if self.board[j,i].decode('utf-8') == SECOND_PLAYER:
                    O_stack.append('c')

            if len(X_stack) == 3:
                return True, True
            if len(O_stack) == 3:
                return True, False

        if self.board[0,0].decode('utf-8') == FIRST_PLAYER and self.board[1,1].decode('utf-8') == FIRST_PLAYER and self.board[2,2].decode('utf-8') == FIRST_PLAYER:
            return True, True
        if self.board[0,2].decode('utf-8') == FIRST_PLAYER and self.board[1,1].decode('utf-8') == FIRST_PLAYER and self.board[2,0].decode('utf-8') == FIRST_PLAYER:
            return True, True
        if self.board[0,0].decode('utf-8') == SECOND_PLAYER and self.board[1,1].decode('utf-8') == SECOND_PLAYER and self.board[2,2].decode('utf-8') == SECOND_PLAYER:
            return True, False
        if self.board[0,2].decode('utf-8') == SECOND_PLAYER and self.board[1,1].decode('utf-8') == SECOND_PLAYER and self.board[2,0].decode('utf-8') == SECOND_PLAYER:
            return True, False

        if EMPTY not in self.board.decode('utf-8'):
            return True, None
        else:
            return False, None

    def reset(self):
        self.board = np.chararray((3,3))
        self.board[:] = EMPTY
        self.started = False

        