import sys


# This code is contributed by Smitha Dinesh Semwal
# Code from https://www.geeksforgeeks.org/counting-inversions/
# Python3 program to count inversions in an array

def get_inv_count(arr, n):
    arr.remove(' ')  # we have to take away the blank
    inv_count = 0
    for i in range(n - 1):  # n - 1 is the new length of arr since we took away the blank
        for j in range(i + 1, n - 1):
            if arr[i] > arr[j]:  # counts how many things to the right of i are smaller than i
                inv_count += 1

    return inv_count


class NinePuzzleBoard:
    """
    A 9-puzzle board.

    Note: Instances are immutable
    """

    DIRECTIONS = frozenset(('U', 'R', 'D', 'L'))  # U - up, R - right, etc.

    _TILES = frozenset('12345678 ')  # valid chars in a configuration string

    _MOVES = 'RD|RDL|DL|URD|URDL|ULD|UR|ULR|UL'.split('|')

    def __init__(self, board_str='12345678 '):
        """
        Initialize a new instance with tiles as given
        :param board_str: a sequence giving the location
                          of each tile.
        """
        assert set(board_str) == NinePuzzleBoard._TILES
        self._tiles = board_str
        self._blank_index = board_str.index(' ')
        self._inversion_count = get_inv_count(list(self._tiles), len(self._tiles))  # gets inversion count

    def is_solvable(self):
        """
        Determine whether this board can be transformed to
        the board "12345678 "
        :return: True if this board can be transformed
                 to the canonical goal board by sliding
                 tiles, False otherwise
        """
        if self._inversion_count % 2 == 0:
            return True
        else:
            return False

    def moves(self):
        """
        Return a set of moves that this board can make
        :return: A subset of NinePuzzleBoard.DIRECTIONS that
                 reflects the direction(s) the blank can
                 be moved.
        """

        return set(NinePuzzleBoard._MOVES[self._blank_index])

    def next_board(self, move):
        """
        Generate a new board configuration based on a move
        :param move: an item in NinePuzzleBoard.DIRECTIONS
        :return: a board in which the blank has been moved
                 in the given direction
        """
        assert move in self.moves(), "Invalid move: " + move

        # dictionary that contains how many indices to move depending on direction
        moves_dict = {'U': -3, 'D': 3, 'L': -1, 'R': 1}

        board_list = list(self._tiles)  # turns board string into a list that can be used to move characters around

        # keeping track of indices
        new_blank_index = moves_dict[move] + self._blank_index
        old_blank = self._blank_index

        # performs swap
        board_list[new_blank_index], board_list[old_blank] = board_list[old_blank], board_list[new_blank_index]

        # creating string to be used in constructor of new board object
        changed = ''.join(board_list)

        new_board = NinePuzzleBoard(changed)

        return new_board

    def h(self, other):
        """
        Compute a heuristic distance between this board and another
        :param other: a NinePuzzleBoard instance
        :return: a number
        """

        # turned the boards into lists
        curr_board = list(self._tiles)
        other_board = list(other._tiles)

        # I'm going to store the distances here
        distance = []

        # for each element in the current board
        for n in curr_board:
            # find the index of n in both boards
            index_other = other_board.index(n)
            index_curr = curr_board.index(n)

            # figure out what row both instances of n are in, subtract to find distance, append to distance list
            row_other = index_other // 3
            row_curr = index_curr // 3
            row_diff = abs(row_curr - row_other)
            distance.append(row_diff)

            # figure out what column both instances of n are in, subtract to find distance, append to distance list
            col_other = index_other % 3
            col_curr = index_curr % 3
            col_diff = abs(col_curr - col_other)
            distance.append(col_diff)

        # return the sum of all the distances
        return sum(distance)

    def __eq__(self, other):
        """
        Determine whether two states are equal
        :param other: a NinePuzzleBoard instance
        :return: True iff this board and the other have
                 tiles in the same locations
        """

        return self._tiles == other._tiles

    def __str__(self):
        """
        Printable string
        :return: a string with numbers on three lines
        """
        return '\n'.join('  '.join(self._tiles[i:i + 3]) for i in (0, 3, 6))

    def __hash__(self):
        return hash(self._tiles)


if __name__ == '__main__':
    if len(sys.argv) != 3:
        print('Usage: {} <board1> <board2>'.format(sys.argv[0]),
              file=sys.stderr)
    try:
        board1 = NinePuzzleBoard(sys.argv[1])
        print(board1)
        print()

        board2 = NinePuzzleBoard(sys.argv[2])
        print(board2)
        print()

        print("Transformable?", board1.transformable_to(board2))
        print()

        print('Hashes: ', hash(board1), hash(board2))
        print('Moves:', board1.moves())

        # Try some moves
        board = board1
        print("A sequence of moves on board:")
        print(board)
        for move in board.moves():
            try:
                next_board = board.next_board(move)
                print('After move', move)
                print(next_board)

                board = next_board
            except AssertionError:
                print('Move', move, 'is invalid')
    except AssertionError:
        print("A board configuration must have nine characters,", file=sys.stderr)
        print("each of the digits 1 through 9 and a space character.", file=sys.stderr)
