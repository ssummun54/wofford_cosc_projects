#ifndef SUDOKU_SOLVER_SUDOKU_H
#define SUDOKU_SOLVER_SUDOKU_H

#include <string>
#include <vector>

using namespace std;


class SudokuBoard {
public:
    class BoardLocation {
    public:
        BoardLocation(int r, int c) : row(r), col(c) {}
        const int row;
        const int col;
        int linearized() const { return row * 9 + col; }
    };
    
    SudokuBoard(const string &start_config);

    bool solved() const;

    bool slot_is_empty(const BoardLocation &location) const;

    BoardLocation next_empty_slot() const;

    void place(char digit, const BoardLocation &location) throw (logic_error);

    void unplace(const BoardLocation &location);

private:
    vector<char> _board;
    friend ostream &operator<<(ostream &os, const SudokuBoard &board);
};

ostream &operator<<(ostream &os, const SudokuBoard &board);

#endif //SUDOKU_SOLVER_SUDOKU_H
