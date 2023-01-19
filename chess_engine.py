class GameState:
    def __init__(self):
        # bR = black Rook, bN = black Knight, bB = black Bishop
        # bQ = black Queen, bK = black King, bP = black Pawn
        self.board = [
            ['bR', 'bN', 'bB', 'bQ', 'bK', 'bB', 'bN', 'bR'],
            ['bP', 'bP', 'bP', 'bP', 'bP', 'bP', 'bP', 'bP'],
            ['--', '--', '--', '--', '--', '--', '--', '--'],
            ['--', '--', '--', '--', '--', '--', '--', '--'],
            ['--', '--', '--', '--', '--', '--', '--', '--'],
            ['--', '--', '--', '--', '--', '--', '--', '--'],
            ['wP', 'wP', 'wP', 'wP', 'wP', 'wP', 'wP', 'wP'],
            ['wR', 'wN', 'wB', 'wQ', 'wK', 'wB', 'wN', 'wR'],
        ]
        self.white_turn = True
        self.move_log = []

    def make_move(self, my_move):
        self.board[my_move.start_row][my_move.start_col] = '--'
        self.board[my_move.end_row][my_move.end_col] = my_move.start
        self.move_log.append(my_move)
        self.white_turn = not self.white_turn


class Move:
    RANK_TO_ROW = {
        '1': 7, '2': 6, '3': 5, '4': 4,
        '5': 3, '6': 2, '7': 1, '8': 0
    }
    ROW_TO_RANK = {v: k for k, v in RANK_TO_ROW.items()}
    FILE_TO_COL = {
        'a': 0, 'b': 1, 'c': 2, 'd': 3,
        'e': 4, 'f': 5, 'g': 6, 'h': 7
    }
    COL_TO_FILE = {v: k for k, v in FILE_TO_COL.items()}

    def __init__(self, start, end, board):
        self.start_row = start[0]
        self.start_col = start[1]
        self.end_row = end[0]
        self.end_col = end[1]
        self.start = board[self.start_row][self.start_col]
        self.end = board[self.end_row][self.end_col]

    def get_chess_notation(self):
        return self.COL_TO_FILE[self.start_col] + self.ROW_TO_RANK[self.start_row] + \
               self.COL_TO_FILE[self.end_col] + self.ROW_TO_RANK[self.end_row]
