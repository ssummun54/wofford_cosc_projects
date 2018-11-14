def solve(sudoku_board, debug=False):
    """
    Solve a Sudoku puzzle
    :param sudoku_board: a SudokuBoard object
    :param debug: If True, prints the board passed to this function
                  and any steps taken in the solution
    :return: True if the puzzle is solved, False otherwise.
             The board has its empty slots filled
    """

    if debug:
        print('SOLVE:')
        print(sudoku_board)

    if not sudoku_board.solved():
        # Find the first empty square
        row, column = sudoku_board.next_empty_slot()
        # for digit in 1, 2, 3, 4, 5, 6, 7, 8, 9:
        for digit in range(1, 10):
            # place digit in the empty square
            try:
                sudoku_board.place(str(digit), row, column)
                #   if debug then print('Placed ', digit, ' in square')
                if debug:
                    print("Placed ", digit, " in square")
                    # if solve(board, debug) is True:
                if solve(sudoku_board, debug):
                    #       if debug then print('SOLVED! Returning True')
                    if debug:
                        print('SOLVED! Returning True')
                        #   return True
                    return True
                # erase digit from the square

                sudoku_board.unplace(row, column)
                # if debug then print('FAIL. Erased ', digit, ' from square')
                if debug:
                    print('FAIL. ERASED ', digit, ' from square')

            except ValueError:
                if debug:
                    print('Did not like', digit, 'in square')
                pass

            # if debug then print('Returning False')
            if debug:
                print('Returning False')
        return False


    else:
        print('RETURNING True')
        return True
