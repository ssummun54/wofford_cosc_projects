//
// Created by ___________
//
#include <iostream>
using namespace std;

#include "sudokusolver.h"

bool solve(SudokuBoard &sudoku_board) {


//    if not sudoku_board.solved():
    if(! sudoku_board.solved()){
        SudokuBoard::BoardLocation location = sudoku_board.next_empty_slot();
        for (char c = '1'; c <= '9'; ++c) {
            try{
                sudoku_board.place(c,location);
                if(solve(sudoku_board)){
                    return true;
                }
                sudoku_board.unplace(location);
            }
            catch (logic_error e){
                continue;
            }
        }
        return false;
    }
    else{
        return true;
    }
//# Find the first empty square
//    row, column = sudoku_board.next_empty_slot()
//# for digit in 1, 2, 3, 4, 5, 6, 7, 8, 9:
//    for digit in range(1, 10):
//# place digit in the empty square
//    try:
//    sudoku_board.place(str(digit), row, column)
//
//                    # if solve(board, debug) is True:
//                if solve(sudoku_board, debug):
//
//                    return True
//                # erase digit from the square
//
//                sudoku_board.unplace(row, column)
//
//
//            except ValueError:
//
//                pass
//
//
//        return False
//
//
//    else:
//        print('RETURNING True')
//        return True

}
