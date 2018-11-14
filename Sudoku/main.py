
import argparse
import sys
import os
import itertools

from sudoku import SudokuBoard
import sudokusolver


def main():

    # Process command line args
    parser = argparse.ArgumentParser(description="Sudoku Solver args",
                                     usage="Usage: {} "
                                           "<puzzle file name>".format(os.path.split(sys.argv[0])[1]),
                                     prog=os.path.split(sys.argv[0])[1])
    parser.add_argument('--debug', dest='debug', default=False, action='store_true')
    parser.add_argument('file_name')
    args = parser.parse_args()

    file_name = args.file_name
    with open(file_name) as puzzle_file:
        # Read nine lines
        data = [puzzle_file.readline().strip() for i in range(9)]
    puzzle = SudokuBoard(itertools.chain(*data))
    print('PUZZLE:')
    print(puzzle)
    print()

    if sudokusolver.solve(puzzle, args.debug):
        print('SOLUTION:')
        print(puzzle)
    else:
        print('Could not find a solution')


if __name__ == '__main__':
    main()
