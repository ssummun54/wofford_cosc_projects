//
// Created by Sykes, David A on 11/13/17.
//
#include <iostream>
#include <algorithm>
#include <stdexcept>
using namespace std;

#include "sudoku.h"

typedef vector<char> CharVector;

SudokuBoard::SudokuBoard(const string &start_config)
    : _board(start_config.begin(), start_config.end())  //INITIALIZER LIST
{
    replace(_board.begin(), _board.end(), '0', ' ');  // Replaces 0s with spaces
}

bool SudokuBoard::solved() const {
    return find(_board.begin(), _board.end(), ' ') == _board.end();
}

bool SudokuBoard::slot_is_empty(const BoardLocation &location) const {
    return _board[location.linearized()] == ' ';
}

SudokuBoard::BoardLocation SudokuBoard::next_empty_slot() const {
    auto it = find(_board.begin(), _board.end(), ' ');
    int index = it - _board.begin();
    return BoardLocation(index / 9, index % 9);
}

void SudokuBoard::place(char digit, const BoardLocation &location) throw (logic_error) {
    if (! slot_is_empty(location)) {
        throw logic_error("Attempt to place a number in an occupied slot");
    }

    int row = location.row;
    int col = location.col;

    // Verify the digit is unique in the row
    auto row_begin_iterator = _board.begin() + row * 9;
    auto row_end_iterator = row_begin_iterator + 9;
    auto it = find(row_begin_iterator, row_end_iterator, digit);
    if ( it != row_end_iterator) {
        throw logic_error("Number in same row");
    }

    // Verify the digit is unique in the column
    for (int i = col; i < 81; i += 9) {
        if (_board[i] == digit) {
            throw logic_error("Number in same column");
        }
    }

    // Verify the digit is unique in the sub-board
    // To check a sub-board, determine the index in _board
    // of the upper left square in it
    int k = ((row / 3) * 3) * 9 + (col / 3) * 3;
    int offsets[] = {0, 1, 2, 9, 10, 11, 18, 19, 20};
    for (auto i: offsets) {
        if (_board[k + i] == digit) {
            throw logic_error("Number in same sub-board");
        }
    }

    // Good to go!
    _board[location.linearized()] = digit;
}

void SudokuBoard::unplace(const BoardLocation &location) {
    _board[location.linearized()] = ' ';
}

ostream &operator<<(ostream &os, const SudokuBoard &board) {
    string frame(" . . .| . . .| . . .\n . . .| . . .| . . .\n . . .| . . .| . . .\n"
                 "------+------+------\n"
                 " . . .| . . .| . . .\n . . .| . . .| . . .\n . . .| . . .| . . .\n"
                 "------+------+------\n"
                 " . . .| . . .| . . .\n . . .| . . .| . . .\n . . .| . . .| . . .");
    // Replace each period in the frame with a digit or space
    int i = 0;
    for (int j = 0; j < frame.size(); ++j) {
        if (frame[j] == '.') {
            frame[j] = board._board[i];
            ++i;
        }
    }
    return os << frame;
}
