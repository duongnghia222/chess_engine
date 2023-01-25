class GameState:
    def __init__(self):
        # bR = black Rook, bN = black Knight, bB = black Bishop
        # bQ = black Queen, bK = black King, bP = black Pawn
        self.board = [
            ['bR', 'bN', 'bB', 'bQ', 'bK', 'bB', 'bN', 'bR'],
            ['bP', 'bP', 'bP', 'bP', 'bP', 'bP', 'bP', 'bP'],
            ['--', '--', '--', '--', '--', '--', '--', '--'],
            ['--', '--', '--', '--', '--', 'wR', '--', '--'],
            ['bR', '--', '--', '--', '--', '--', '--', '--'],
            ['--', '--', '--', 'bP', '--', '--', '--', '--'],
            ['wP', 'wP', 'wP', 'wP', 'wP', 'wP', 'wP', 'wP'],
            ['wR', 'wN', 'wB', 'wQ', 'wK', 'wB', 'wN', 'wR'],
        ]
        self.move_function = {'P': self.get_pawn_move, 'R': self.get_rook_move,
                              'N': self.get_knight_move, 'Q': self.get_queen_move,
                              'K': self.get_king_move}
        self.white_turn = True
        self.move_log = []
        self.white_king_position = (7, 4)
        self.black_king_position = (0, 4)
        self.checkmate = False
        self.stalemate = False


    def make_move(self, my_move):
        self.board[my_move.start_row][my_move.start_col] = '--'
        self.board[my_move.end_row][my_move.end_col] = my_move.start
        self.move_log.append(my_move)
        self.white_turn = not self.white_turn
        if my_move.start == 'wK':
            self.white_king_position = (my_move.end_row, my_move.end_col)
        elif my_move.start == 'bK':
            self.black_king_position = (my_move.end_row, my_move.end_col)

    def undo_move(self):
        if len(self.move_log) == 0:
            return
        last_move = self.move_log.pop()
        self.board[last_move.start_row][last_move.start_col] = last_move.start
        self.board[last_move.end_row][last_move.end_col] = last_move.end
        self.white_turn = not self.white_turn
        if last_move.start == 'wK':
            self.white_king_position = (last_move.start_row, last_move.start_col)
        elif last_move.start == 'bK':
            self.black_king_position = (last_move.start_row, last_move.start_col)

    def get_valid_moves(self):
        valid_moves = self.get_all_possible_move()
        for i in range(len(valid_moves) - 1, -1, -1):
            self.make_move(valid_moves[i])
            self.white_turn = not self.white_turn
            if self.if_in_check():
                valid_moves.remove(valid_moves[i])
            self.white_turn = not self.white_turn
            self.undo_move()
        if len(valid_moves) == 0:
            if self.if_in_check():
                self.checkmate = True
            else:
                self.stalemate = True
        return valid_moves

    def if_in_check(self):
        if self.white_turn:
            return self.square_under_check_at_r_c(self.white_king_position[0], self.white_king_position[1])
        else:
            return self.square_under_check_at_r_c(self.black_king_position[0], self.black_king_position[1])

    def square_under_check_at_r_c(self, r, c):
        self.white_turn = not self.white_turn
        opponent_moves = self.get_all_possible_move()
        self.white_turn = not self.white_turn
        for om in opponent_moves:
            if om.end_row == r and om.end_col == c:
                return True
        return False

    def get_all_possible_move(self):
        possible_moves = []
        for r in range(8):
            for c in range(8):
                turn = self.board[r][c][0]
                if (turn == 'w' and self.white_turn) or (turn == 'b' and not self.white_turn):
                    piece = self.board[r][c][1]
                    if piece == 'P':
                        self.get_pawn_move(r, c, possible_moves)
                    elif piece == 'R':
                        self.get_rook_move(r, c, possible_moves)
                    elif piece == 'N':
                        self.get_knight_move(r, c, possible_moves)
                    elif piece == 'B':
                        self.get_bishop_move(r, c, possible_moves)
                    elif piece == 'Q':
                        self.get_queen_move(r, c, possible_moves)
                    elif piece == 'K':
                        self.get_king_move(r, c, possible_moves)
        return possible_moves

    def get_pawn_move(self, r, c, possible_moves):
        if self.white_turn:
            if self.board[r-1][c] == '--':
                possible_moves.append(Move((r, c), (r-1, c), self.board))
                if r == 6 and self.board[r-2][c] == '--':
                    possible_moves.append(Move((r, c), (r-2, c), self.board))
            if c - 1 >= 0:
                if self.board[r-1][c-1][0] == 'b':
                    possible_moves.append(Move((r, c), (r-1, c-1), self.board))
            if c + 1 <= 7:
                if self.board[r-1][c+1][0] == 'b':
                    possible_moves.append(Move((r, c), (r-1, c+1), self.board))
        else:
            if self.board[r+1][c] == '--':
                possible_moves.append(Move((r, c), (r+1, c), self.board))
                if r == 1 and self.board[r+2][c] == '--':
                    possible_moves.append(Move((r, c), (r+2, c), self.board))
            if c - 1 >= 0:
                if self.board[r+1][c-1][0] == 'w':
                    possible_moves.append(Move((r, c), (r+1, c-1), self.board))
            if c + 1 <= 7:
                if self.board[r+1][c+1][0] == 'w':
                    possible_moves.append(Move((r, c), (r+1, c+1), self.board))

    def get_rook_move(self, row, col, possible_moves):
        directions = ((1, 0), (0, 1), (-1, 0), (0, -1))
        enemy = 'b' if self.white_turn else 'w'
        for d in directions:
            for i in range(1, 8):
                end_row = row + d[0] * i
                end_col = col + d[1] * i
                if 0 <= end_col <= 7 and 0 <= end_row <= 7 and \
                        (self.board[end_row][end_col][0] == enemy or self.board[end_row][end_col] == '--'):
                    possible_moves.append(Move((row, col), (end_row, end_col), self.board))
                    if self.board[end_row][end_col][0] == enemy:
                        break
                else:
                    break
            else:
                continue
            continue

    def get_knight_move(self, row, col, possible_moves):
        directions = ((-2, -1), (2, -1), (-2, 1), (2, 1), (-1, -2), (1, -2), (-1, 2), (1, 2))
        enemy = 'b' if self.white_turn else 'w'
        for d in directions:
            end_row = row + d[0]
            end_col = col + d[1]
            if 0 <= end_col <= 7 and 0 <= end_row <= 7 and \
                    (self.board[end_row][end_col][0] == enemy or self.board[end_row][end_col] == '--'):
                possible_moves.append(Move((row, col), (end_row, end_col), self.board))

    def get_bishop_move(self, row, col, possible_moves):
        directions = ((-1, -1), (1, 1), (-1, 1), (1, -1))
        enemy = 'b' if self.white_turn else 'w'
        for d in directions:
            for i in range(1, 8):
                end_row = row + d[0] * i
                end_col = col + d[1] * i
                if 0 <= end_col <= 7 and 0 <= end_row <= 7 and \
                        (self.board[end_row][end_col][0] == enemy or self.board[end_row][end_col] == '--'):
                    possible_moves.append(Move((row, col), (end_row, end_col), self.board))
                    if self.board[end_row][end_col][0] == enemy:
                        break
                else:
                    break
            else:
                continue
            continue

    def get_queen_move(self, row, col, possible_moves):
        self.get_rook_move(row, col, possible_moves)
        self.get_bishop_move(row, col, possible_moves)

    def get_king_move(self, row, col, possible_moves):
        directions = ((1, 0), (0, 1), (-1, 0), (0, -1), (-1, -1), (1, 1), (-1, 1), (1, -1))
        enemy = 'b' if self.white_turn else 'w'
        for d in directions:
            end_row = row + d[0]
            end_col = col + d[1]
            if 0 <= end_col <= 7 and 0 <= end_row <= 7 and \
                    (self.board[end_row][end_col][0] == enemy or self.board[end_row][end_col] == '--'):
                possible_moves.append(Move((row, col), (end_row, end_col), self.board))


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
        self.moveID = self.start_row*1000 + 100*self.start_col + 10*self.end_row + self.end_col

    def __eq__(self, other):
        if isinstance(other, Move):
            return self.moveID == other.moveID
        return False

    def get_chess_notation(self):
        return self.COL_TO_FILE[self.start_col] + self.ROW_TO_RANK[self.start_row] + \
               self.COL_TO_FILE[self.end_col] + self.ROW_TO_RANK[self.end_row]
