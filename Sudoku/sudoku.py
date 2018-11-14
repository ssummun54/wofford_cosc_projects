"""
This module defines a Sudoku Board ADT
"""


class SudokuBoard:

    def __init__(self, start_config):
        """
        Load this board from the given file
        :param start_config: a sequence of digits that give the
                             start board configuration. A zero
                            indicates a blank slot. The slots
                            are processed left-to-right, top-
                            to-bottom. Note: a digit is a string
                            '0', '1', '2', ..., '9'
        :raise: ValueError if a slot is invalid
        """


        # Construct a list of 81 empty slots
        self._board = [' ' for i in range(9 * 9)]
        for i, slot in enumerate(start_config):
            if slot != '0':
                self.place(slot, i // 9, i % 9)
    #def solve(sudoku_board, debug=False):
        # """
        # Solve a Sudoku puzzle
        # :param sudoku_board: a SudokuBoard object
        # :param debug: If True, prints the board passed to this function
        #               and any steps taken in the solution
        # :return: True if the puzzle is solved, False otherwise.
        #          The board has its empty slots filled
        # """

        # if debug:
        #     print('SOLVE:')
        #     print(sudoku_board)
        #
        # if not sudoku_board.solved():
        #     # Find the first empty square
        #     row, column = sudoku_board.next_empty_slot()
        #     # for digit in 1, 2, 3, 4, 5, 6, 7, 8, 9:
        #     for digit in range(1, 10):
        #         # place digit in the empty square
        #         sudoku_board.place(digit, row, column)
        #         #    if debug then print('Placed ', digit, ' in square')
        #         if debug:
        #             print("Placed ", digit, " in square")
        #
        #             #    if solve(board, debug) is True:
        #         if solve(sudoku_board, debug):
        #             #       if debug then print('SOLVED! Returning True')
        #             if debug:
        #                 print('SOLVED! Returning True')
        #                 #         return True
        #                 return True
        #
        #         # erase digit from the square
        #         sudoku_board.unplace(row, column)
        #         # if debug then print('FAIL. Erased ', digit, ' from square')
        #         if debug:
        #             print('FAIL. ERASED ', digit, ' from square')
        #
        #     # if debug then print('Returning False')
        #     if debug:
        #         print('Returning False')
        #         return False
        #
        # else:
        #     print('RETURNING True')
        #     return True
    def solved(self):
        """
        Determine if this puzzle is solved
        :return: True if solved (no empty slots), False otherwise
        """
        try:
            # A puzzle is solved if there are no spaces in self._board
            self._board.index(' ')
            return False
        except ValueError:
            return True
        # Could also use return self._board.count(' ') == 0

    def slot_is_empty(self, row, col):
        """
        Determine whether a given slot os empty
        :param row: row number 0-8
        :param col: column number 0-8
        :return: True if the slot at the given row is
                 empty, False otherwise
        """
        return self._board[self._linearize(row, col)] == ' '

    def next_empty_slot(self):
        """
        Return the row and column of the next empty slot
        Precondition: not self.solved()
        :return: (row, col) of the next empty slot
        :raise: ValueError if this puzzle is solved
        """
        k = self._board.index(' ')
        return k // 9, k % 9

    def place(self, digit, row, col):
        """
        Put a digit into an empty slot, but only if the placement is valid
        :param digit: a str value in ('1', '2', ..., '9')
        :param row: row number 0-8
        :param col: column number 0-8
        :return: None
        :raise: Value Error is the slot is already occupied
                or if this placement violates a rule
        """

        if self._board[row * 9 + col] != ' ':
            raise ValueError('row {}, col {} OCCUPIED'.format(row, col))

        # Verify the digit is unique in the row,
        # column, and sub-board
        if digit in self._board[row * 9: row * 9 + 9]:
            raise ValueError('row {}, col {} ROW'.format(row, col))
        if digit in self._board[col: 81: 9]:
            raise ValueError('row {}, col {} COL'.format(row, col))

        # To check a sub-board, determine the index in _board
        # of the upper left square in it
        i = ((row // 3) * 3) * 9 + (col // 3) * 3

        if digit in self._board[i:i + 3] or \
           digit in self._board[i + 9:i + 12] or \
           digit in self._board[i + 18:i + 21]:
            raise ValueError('row {}, col {} SECTION'.format(row, col))

        # Good to go!
        self._board[self._linearize(row, col)] = digit

    def unplace(self, row, col):
        """
        Remove a digit from a slot
        :param row: row number 0-8
        :param col: column number 0-8
        :return: The digit removed or None if no digit occupies that slot
        """
        k = self._linearize(row, col)
        value = self._board[k]
        self._board[k] = ' '
        return value if value != ' ' else None

    def __str__(self):
        """
        Return a string that prints as a 9-by-9 grid
        :return: a string
        """

        frame = '''
 . . .| . . .| . . .
 . . .| . . .| . . .
 . . .| . . .| . . .
------+------+------
 . . .| . . .| . . .
 . . .| . . .| . . .
 . . .| . . .| . . .
------+------+------
 . . .| . . .| . . .
 . . .| . . .| . . .
 . . .| . . .| . . .'''
        frame_list = list(frame)
        i = 0
        for j, slot in enumerate(frame_list):
            if slot == '.':
                frame_list[j] = self._board[i]
                i += 1
        return ''.join(frame_list)

    @classmethod
    def _linearize(cls, row, col):
        """
        Return the index in a board associated with a row and column
        :param row:
        :param col:
        :return: a number between 0 and 80, inclusive
        """
        return row * 9 + col


if __name__ == '__main__':
# Source: https://github.com/codegoalie/sudoku-api9
    b = SudokuBoard('030000050008091300600400700003810000006000200000034800001008009004120600060000040')
    print(b)
    print()
    # b.place('6', 0, 1)  # Occupied
    # b.place('3', 0, 0)  # Row duplicate
    # b.place('6', 0, 0)  # Col duplicate
    # b.place('9', 2, 5)  # Section duplicate
