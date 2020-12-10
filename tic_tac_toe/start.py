import sys
import random
import math


class Game:
    def __init__(self):
        self._board = list()

        # map input coordinates to these used in programming world
        self._coordinates = {
            (1, 3): (0, 1), (2, 3): (0, 2), (3, 3): (0, 3),
            (1, 2): (1, 1), (2, 2): (1, 2), (3, 2): (1, 3),
            (1, 1): (2, 1), (2, 1): (2, 2), (3, 1): (2, 3)
        }

        for _ in range(0, 3):
            board_row = []
            board_row.extend(["|" if i == 0 or i == 4 else " " for i in range(0, 5)])
            self._board.append(board_row)

    def make_move(self, player, symbol):
        return self._user_move(symbol) if player == "user" else self._ai_move(symbol, player)

    def _user_move(self, symbol):
        while True:
            try:
                y, x = map(lambda pos: int(pos), input("Enter the coordinates: ").split())

                valid_coords = [1, 2, 3]
                if y in valid_coords and x in valid_coords:
                    y, x = self._coordinates[(y, x)]
                    if self._board[y][x] != " ":
                        print("This cell is occupied! Choose another one!\n")
                    else:
                        self._board[y][x] = symbol
                        return
                else:
                    print("Coordinates should be from 1 to 3!\n")

            except ValueError:
                print("You should enter numbers!\n")

    def _ai_move(self, symbol, lvl):
        if lvl == "easy":
            self._ai_easy_move(symbol)

        elif lvl == "medium":
            self._ai_medium_move(symbol)

        elif lvl == "hard":
            self._ai_hard_move(symbol)

    def _ai_easy_move(self, symbol):
        print("Making move level \"easy\"\n")

        # get free fields on the board
        free_indexes = [(pos_y, pos_x) for pos_y, row in enumerate(self._board)
                        for pos_x, cell in enumerate(row) if cell == ' ']

        # choose random empty cell and play on it
        pos_y, pos_x = free_indexes[random.randint(0, len(free_indexes) - 1)]
        self._board[pos_y][pos_x] = symbol

    def _ai_medium_move(self, symbol):
        print("Making move level \"medium\"\n")

        # place last one in a row to win the match
        for col, row in enumerate(self._board):
            if row.count(symbol) == 2 and row.count(" "):
                self._board[col][row.index(" ")] = symbol
                return

        # figure out who is opponent
        opponent = "O" if symbol == "X" else "X"

        # block opponent if can win in row
        for col, row in enumerate(self._board):
            if row.count(opponent) == 2 and row.count(" "):
                self._board[col][row.index(" ")] = symbol
                return

        for col_num in range(1, 4):
            column = [col[col_num] for col in self._board]
            if column.count(opponent) == 2 and column.count(" "):
                self._board[column.index(" ")][col_num] = symbol
                return

        diagonal_right = [self._board[i][i + 1] for i in range(len(self._board))]
        diagonal_left = [self._board[i][len(self._board) - i] for i in range(len(self._board))]

        if diagonal_right.count(opponent) == 2 and diagonal_right.count(" "):
            self._board[diagonal_right.index(" ")][diagonal_right.index(" ") + 1] = symbol
            return

        if diagonal_left.count(opponent) == 2 and diagonal_left.count(" "):
            self._board[diagonal_left.index(" ")][abs(diagonal_left.index(" ") - 3)] = symbol
            return

        # cannot both win and block then randomly move
        self._ai_easy_move(symbol)

    def _ai_hard_move(self, symbol):
        pos_y, pos_x = self._find_best_move(self._board, symbol)
        self._board[pos_y][pos_x] = symbol

    def _find_best_move(self, board, symbol):
        best_move = -math.inf
        best_move_coords = (-1, -1)

        for row_num, row in enumerate(board):
            for cell_num, cell in enumerate(row):
                if cell == " ":
                    board[row_num][cell_num] = symbol

                    move_value = self._mini_max(board, False, symbol)
                    board[row_num][cell_num] = " "

                    if move_value > best_move:
                        best_move = move_value
                        best_move_coords = (row_num, cell_num)

        return best_move_coords

    def _mini_max(self, board, is_ai_move, symbol):
        # it's a draw, this will stop recursion
        if not self._is_move_left(board):
            return 0

        # evaluate first move from _find_best_move
        move_value = self._evaluate(board, symbol)

        # return move_value if not a draw
        if move_value:
            return move_value

        if is_ai_move:
            best = -math.inf

            for row_pos, row in enumerate(board):
                for cell_pos, cell in enumerate(row):
                    if cell == " ":
                        board[row_pos][cell_pos] = symbol

                        best = max(self._mini_max(board, not is_ai_move, symbol))
                        board[row_pos][cell_pos] = " "

            return best
        else:
            worst = math.inf

            for row_pos, row in enumerate(board):
                for cell_pos, cell in enumerate(row):
                    if cell == " ":
                        board[row_pos][cell_pos] = "X" if symbol == "O" else "O"

                        worst = min(self._mini_max(board, not is_ai_move, symbol))
                        board[row_pos][cell_pos] = " "

            return worst

    def _is_move_left(self, board):
        return True if board.count(" ") > 0 else False

    def _evaluate(self, board, symbol):
        opponent = "X" if symbol == "O" else "O"

        opponent_is_winner = self.check_state(opponent, True)
        player_is_winner = self.check_state(symbol, True)

        if opponent_is_winner:
            return -10
        elif player_is_winner:
            return 10
        else:
            return 0

    def show_board(self):
        separator = "-" * 9

        print(separator)
        for row in self._board:
            print(*row)
        print(separator)

    def check_state(self, symbol, print_info=False):
        diagonal_right = [self._board[i][i + 1] for i in range(len(self._board))]
        diagonal_left = [self._board[i][len(self._board) - i] for i in range(len(self._board))]

        # there are three in a row or diagonal
        for row in self._board:
            if row.count(symbol) == 3 or diagonal_right.count(symbol) == 3 or diagonal_left.count(symbol) == 3:
                if not print_info:
                    print(symbol, "wins\n")
                return True

        # there are three in column
        for col_num in range(1, 4):
            column = [col[col_num] for col in self._board]
            if column.count(symbol) == 3:
                if not print_info:
                    print(symbol, "wins\n")
                return True

        # no winner - draw
        if not sum(row.count(" ") for row in self._board):
            if not print_info:
                print("Draw\n")
            return True

        # game is still in progress
        return False


def read_user_input():
    cmd = input("Input command: ")
    if cmd == "exit":
        sys.exit()

    try:
        act, pl1, pl2 = cmd.split()

    except ValueError:
        print("Bad parameters!\n")
        return None, None, None

    else:
        return act, pl1, pl2


if __name__ == "__main__":
    game = Game()

    while True:
        action, player_1, player_2 = read_user_input()
        if action:
            if action == "exit":
                sys.exit()
            else:
                game.show_board()
            while True:
                game.make_move(player_1, "X")
                game.show_board()
                if game.check_state("X"):
                    sys.exit()

                game.make_move(player_2, "O")
                game.show_board()
                if game.check_state("O"):
                    sys.exit()
