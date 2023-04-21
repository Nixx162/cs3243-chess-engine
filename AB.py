import sys
from copy import deepcopy
from random import seed, choice

### IMPORTANT: Remove any print() functions or rename any print functions/variables/string when submitting on CodePost
### The autograder will not run if it detects any print function.
start_board = {('a', 1): ('Ferz', 'White'), ('a', 5): ('Ferz', 'Black'), ('g', 1):
('Ferz', 'White'), ('g', 5): ('Ferz', 'Black'), ('b', 1): ('Pawn',
'White'), ('b', 5): ('Pawn', 'Black'), ('c', 1): ('Pawn', 'White'),
('c', 5): ('Pawn', 'Black'), ('d', 1): ('Pawn', 'White'), ('d', 5):
('Pawn', 'Black'), ('e', 1): ('Pawn', 'White'), ('e', 5): ('Pawn',
'Black'), ('f', 1): ('Pawn', 'White'), ('f', 5): ('Pawn', 'Black'),
('a', 0): ('Knight', 'White'), ('a', 6): ('Knight', 'Black'), ('b',
0): ('Bishop', 'White'), ('b', 6): ('Bishop', 'Black'), ('c', 0):
('Queen', 'White'), ('c', 6): ('Queen', 'Black'), ('d', 0): ('King',
'White'), ('d', 6): ('King', 'Black'), ('e', 0): ('Princess', 'White'),
('e', 6): ('Princess', 'Black'), ('f', 0): ('Empress', 'White'),
('f', 6): ('Empress', 'Black'), ('g', 0): ('Rook', 'White'), ('g',
6): ('Rook', 'Black')}
    

# Helper functions to aid in your implementation. Can edit/remove
class State:
    def __init__(self, board = start_board, turn = 0, is_terminal = False):
        self.rows = 7
        self.cols = 7
        self.board = deepcopy(board)
        self.turn = turn
        self.is_terminal = is_terminal

    def in_range(self, col, row):
        if 0 <= row <= self.rows and 'a' <= col <= 'g':
            return True
        
    def valid_move(self, col, row, side):
        if (col, row) not in self.board or self.board[(col, row)][1] != side:
            return True


    def to_move(self):
        return self.turn % 2

    def actions(self, turn):
        turn = ['White', 'Black'][turn]

        out = []

        for (col, row), (piece, side) in self.board.items():
            if side == turn:
                if piece == 'King':
                    for i in range(-1,2):
                        for j in range (-1,2):
                            if i != j or i != 0:
                                if self.in_range(chr(ord(col) + i), row + j) and self.valid_move(chr(ord(col) + i), row + j, side):
                                    out.append(((col, row), (chr(ord(col) + i), row + j)))
                
                if piece in ['Queen', 'Bishop', 'Princess']:
                    for i in range(1,7):
                        if self.in_range(chr(ord(col) - i), row + i):
                            if (chr(ord(col) - i), row + i) not in self.board:
                                out.append(((col, row), (chr(ord(col) - i), row + i)))
                            elif self.board[(chr(ord(col) - i), row + i)][1] != side:
                                out.append(((col, row), (chr(ord(col) - i), row + i)))
                                break
                            else: 
                                break
                        else:
                            break

                    for i in range(1,7):
                        if self.in_range(chr(ord(col) + i), row - i):
                            if (chr(ord(col) + i), row - i) not in self.board:
                                out.append(((col, row), (chr(ord(col) + i), row - i)))
                            elif self.board[(chr(ord(col) + i), row - i)][1] != side:
                                out.append(((col, row), (chr(ord(col) + i), row - i)))
                                break
                            else: 
                                break
                        else:
                            break

                    for i in range(1,7):
                        if self.in_range(chr(ord(col) - i), row - i):
                            if (chr(ord(col) - i), row - i) not in self.board:
                                out.append(((col, row), (chr(ord(col) - i), row - i)))
                            elif self.board[(chr(ord(col) - i), row - i)][1] != side:
                                out.append(((col, row), (chr(ord(col) - i), row - i)))
                                break
                            else: 
                                break
                        else:
                            break

                    for i in range(1,7):
                        if self.in_range(chr(ord(col) + i), row + i):
                            if (chr(ord(col) + i), row + i) not in self.board:
                                out.append(((col, row), (chr(ord(col) + i), row + i)))
                            elif self.board[(chr(ord(col) + i), row + i)][1] != side:
                                out.append(((col, row), (chr(ord(col) + i), row + i)))
                                break
                            else: 
                                break
                        else:
                            break


                if piece in ['Queen', 'Rook', 'Empress']:
                    for i in range(1,7):
                        if self.in_range(chr(ord(col) + i), row):
                            if (chr(ord(col) + i), row) not in self.board:
                                out.append(((col, row), (chr(ord(col) + i), row)))
                            elif self.board[(chr(ord(col) + i), row)][1] != side:
                                out.append(((col, row), (chr(ord(col) + i), row)))
                                break
                            else: 
                                break
                        else:
                            break

                        if self.in_range(chr(ord(col) - i), row):
                            if (chr(ord(col) - i), row) not in self.board:
                                out.append(((col, row), (chr(ord(col) - i), row)))
                            elif self.board[(chr(ord(col) - i), row)][1] != side:
                                out.append(((col, row), (chr(ord(col) - i), row)))
                                break
                            else: 
                                break
                        else:
                            break

                        if self.in_range(col, row + i):
                            if (col, row + i) not in self.board:
                                out.append(((col, row), (col, row + i)))
                            elif self.board[(col, row + i)][1] != side:
                                out.append(((col, row), (col, row + i)))
                                break
                            else: 
                                break
                        else:
                            break

                        if self.in_range(col, row - i):
                            if (col, row - i) not in self.board:
                                out.append(((col, row), (col, row - i)))
                            elif self.board[(col, row - i)][1] != side:
                                out.append(((col, row), (col, row - i)))
                                break
                            else: 
                                break
                        else:
                            break

                if piece in ['Princess', 'Empress', 'Knight']:
                    for i, j in ((1, 2), (1, -2), (2, 1), (2, -1), (-1, 2), (-1, -2), (-2, 1), (-2, -1)):
                        if self.in_range(chr(ord(col) + i), row + j) and self.valid_move(chr(ord(col) + i), row + j, side):
                            out.append(((col, row), (chr(ord(col) + i), row + j)))

                if piece == 'Pawn':
                    if turn == 'White':
                        if self.in_range(col, row + 1):
                            if (col, row + 1) not in self.board:
                                out.append(((col, row), (col, row + 1)))

                        if self.in_range(chr(ord(col) + 1), row + 1):
                            if (chr(ord(col) + 1), row + 1) in self.board and self.board[(chr(ord(col) + 1), row + 1)][1] != side: 
                                out.append(((col, row), (chr(ord(col) + 1), row + 1)))

                        if self.in_range(chr(ord(col) - 1), row + 1):
                            if (chr(ord(col) - 1), row + 1) in self.board and self.board[(chr(ord(col) - 1), row + 1)][1] != side: 
                                out.append(((col, row), (chr(ord(col) - 1), row + 1)))

                    else:
                        if self.in_range(col, row - 1):
                            if (col, row - 1) not in self.board:
                                out.append(((col, row), (col, row - 1)))

                        if self.in_range(chr(ord(col) + 1), row - 1):
                            if (chr(ord(col) + 1), row - 1) in self.board and self.board[(chr(ord(col) + 1), row - 1)][1] != side: 
                                out.append(((col, row), (chr(ord(col) + 1), row - 1)))

                        if self.in_range(chr(ord(col) - 1), row - 1):
                            if (chr(ord(col) - 1), row - 1) in self.board and self.board[(chr(ord(col) - 1), row - 1)][1] != side: 
                                out.append(((col, row), (chr(ord(col) - 1), row - 1)))

                if piece == 'Ferz':
                    if self.in_range(chr(ord(col) + 1), row + 1) and self.valid_move(chr(ord(col) + 1), row + 1, side):
                        out.append(((col, row), (chr(ord(col) + 1), row + 1)))

                    if self.in_range(chr(ord(col) + 1), row - 1) and self.valid_move(chr(ord(col) + 1), row - 1, side):
                        out.append(((col, row), (chr(ord(col) + 1), row - 1)))

                    if self.in_range(chr(ord(col) - 1), row + 1) and self.valid_move(chr(ord(col) - 1), row + 1, side):
                        out.append(((col, row), (chr(ord(col) - 1), row + 1)))

                    if self.in_range(chr(ord(col) - 1), row - 1) and self.valid_move(chr(ord(col) - 1), row - 1, side):
                        out.append(((col, row), (chr(ord(col) - 1), row - 1)))
                        
        return out
    
    def move(self, delta):
        out = State(self.board, (self.turn + 1) % 2, self.is_terminal)
        if delta:
            if delta[1] in out.board and out.board[delta[1]][0] == 'King':
                out.is_terminal = True
            out.board[delta[1]] = out.board[delta[0]]
            out.board.pop(delta[0])
        return out

    def utility(self):
        weight = {
            'King': 40,
            'Queen': 9,
            'Empress': 7,
            'Princess': 7,
            'Rook': 5,
            'Bishop': 3,
            'Knight': 3,
            'Ferz': 2,
            'Pawn': 1,
            'Mobility': 0.1
        }

        counts = {
            'King': 0,
            'Queen': 0,
            'Empress': 0,
            'Princess': 0,
            'Rook': 0,
            'Bishop': 0,
            'Knight': 0,
            'Ferz': 0,
            'Pawn': 0,
            'Mobility': len(self.actions(0)) - len(self.actions(1))
        }

        val = 0

        for piece, side in self.board.values():
            if side == 'White':
                counts[piece] += 1
            else:
                counts[piece] -= 1

        for k in counts:
            val += weight[k] * counts[k]
        return val
    
def max_val(state, alpha, beta, depth):
    if state.is_terminal or depth == 0:
        return state.utility(), None
    val = -float('inf')
    for delta in state.actions(state.turn):
        val1, _ = min_val(state.move(delta), alpha, beta, depth - 1)
        if val1 > val:
            val, move = val1, delta
            alpha = max(alpha, val)
        if val >= beta:
            return val, move
    return val, move

def min_val(state, alpha, beta, depth):
    if state.is_terminal or depth == 0:
        return state.utility(), None
    val = float('inf')
    for delta in state.actions(state.turn):
        val1, _ = max_val(state.move(delta), alpha, beta, depth - 1)
        if val1 < val:
            val, move = val1, delta
            beta = min(beta, val)
        if val <= alpha:
            return val, move
    return val, move

def parse(move):
    temp = move
    temp[0][0] = chr(ord('a') + temp[0][0])
    temp[1][0] = chr(ord('a')+ temp[1][0])
    return temp
  

#Implement your minimax with alpha-beta pruning algorithm here.
def ab(state):
    seed(69696)
    d = choice([2, 2, 2, 2, 2, 2, 3, 3])
    _, move = max_val(state, -float('inf'), float('inf'), d)
    return move



### DO NOT EDIT/REMOVE THE FUNCTION HEADER BELOW###
# Chess Pieces: King, Queen, Knight, Bishop, Rook (First letter capitalized)
# Colours: White, Black (First Letter capitalized)
# Positions: Tuple. (column (String format), row (Int)). Example: ('a', 0)

# Parameters:
# gameboard: Dictionary of positions (Key) to the tuple of piece type and its colour (Value). This represents the current pieces left on the board.
# Key: position is a tuple with the x-axis in String format and the y-axis in integer format.
# Value: tuple of piece type and piece colour with both values being in String format. Note that the first letter for both type and colour are capitalized as well.
# gameboard example: {('a', 0) : ('Queen', 'White'), ('d', 10) : ('Knight', 'Black'), ('g', 25) : ('Rook', 'White')}
#
# Return value:
# move: A tuple containing the starting position of the piece being moved to the new position for the piece. x-axis in String format and y-axis in integer format.
# move example: (('a', 0), ('b', 3))

def studentAgent(gameboard):
    move = ab(State(gameboard, 0))
    return move #Format to be returned (('a', 0), ('b', 3))
