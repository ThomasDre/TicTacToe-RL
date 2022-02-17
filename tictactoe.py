import numpy as np

X_PLAYER = 'X'
O_PLAYER = '0'
EMPTY = '-'

class TicTacToe:
    def __init__(self):
        self.board = np.chararray((3,3))
        self.started = False
        self.active_player = X_PLAYER
        self.state_space =  1024 # take times 2 because x - o and o - x are counted individually
        self.action_space = 9

        self.board[:] = EMPTY

    def set_cell(self, is_first, sign, x, y):
        """
        Makes a move if admissible
        """

        # TODO we need a reward signal. E.g. invalid moves -1000, won +1, neutral move 0 and tie maybe something inbetween, lose -1

        if is_first and self.active_player != X_PLAYER:
            print("OOPS")
            return False

        if self.board[x,y].decode('utf-8') == EMPTY:
            #sign = X_PLAYER if is_first else O_PLAYER
            self.board[x,y] = sign
            self.started = True

            self.active_player = O_PLAYER if self.active_player == X_PLAYER else X_PLAYER

            has_ended, status = self.check_game()

            return True
        else:
            return False

    def check_game(self):
        """
        Cheks whether the game ended, and who won or whether there was a draw
        Returns tuple of (hasEnded, status)

        where status == True means X_PLAYER (X) won, status == False means O_PLAYER (0) won, and status == None means there was a draw
        """
        for i in range(3):
            X_stack = []
            O_stack = []

            for j in range(3):
                if self.board[i,j].decode('utf-8') == X_PLAYER:
                    X_stack.append('c')
                if self.board[i,j].decode('utf-8') == O_PLAYER:
                    O_stack.append('c')

            if len(X_stack) == 3:
                return True, True
            if len(O_stack) == 3:
                return True, False

            X_stack = []
            O_stack = []

            for j in range(3):
                if self.board[j,i].decode('utf-8') == X_PLAYER:
                    X_stack.append('c')
                if self.board[j,i].decode('utf-8') == O_PLAYER:
                    O_stack.append('c')

            if len(X_stack) == 3:
                return True, True
            if len(O_stack) == 3:
                return True, False

        if self.board[0,0].decode('utf-8') == X_PLAYER and self.board[1,1].decode('utf-8') == X_PLAYER and self.board[2,2].decode('utf-8') == X_PLAYER:
            return True, True
        if self.board[0,2].decode('utf-8') == X_PLAYER and self.board[1,1].decode('utf-8') == X_PLAYER and self.board[2,0].decode('utf-8') == X_PLAYER:
            return True, True
        if self.board[0,0].decode('utf-8') == O_PLAYER and self.board[1,1].decode('utf-8') == O_PLAYER and self.board[2,2].decode('utf-8') == O_PLAYER:
            return True, False
        if self.board[0,2].decode('utf-8') == O_PLAYER and self.board[1,1].decode('utf-8') == O_PLAYER and self.board[2,0].decode('utf-8') == O_PLAYER:
            return True, False

        if EMPTY not in self.board.decode('utf-8'):
            return True, None
        else:
            return False, None     

    def reset(self):
        self.board = np.chararray((3,3))
        self.board[:] = EMPTY
        self.started = False

    def get_possible_moves(self):
        moves = []

        for i in range(3):
            for j in range(3):
                if self.board[x,y].decode('utf-8') == EMPTY:
                    moves.append((i,j))

        return moves

    def get_num_of_state(self):
        """
        TODO IMPLEMENT ME
        given that a tic tac board has N states (state_space). Each state is one of these N states.
        This function maps the current state of the board to the n-th state

        e.g. - - -                          X - -                         etc  
             - - -                          - - -
             - - -                          - - -
 
             represents the 0-th state      represents the 1-th state
        """
        pass

    def selected_action_to_move(self, action):
        """
        returnx cell to be marked. a cell is reprented by x and y
        :param action the selected action [0;8]
        """
        x = action // 3
        y = action % 3

        return (x,y)
