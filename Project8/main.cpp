#include <iostream>
#include <fstream>
#include <string>

using namespace std;

#include "sudoku.h"
#include "sudokusolver.h"


int main(int argc, const char **argv) {
    if (argc != 2) {
        cerr << "Usage: " << argv[0] << " <puzzle file name>" << endl;
        exit(1);
    }

    // Open the puzzle file
    ifstream puzzle_file(argv[1], ifstream::in);
    if (! puzzle_file.is_open()) {
        cerr << "Could not open file " << argv[1] << endl;
        exit(2);
    }

    // Read nine lines to get a string of 81 digits
    // A zero represents a blank slot
    string puzzle;
    string line;
    for (int i = 0; i < 9; ++i) {
        getline(puzzle_file, line);
        puzzle += line;
    }
    puzzle_file.close();

    // Create a board using the data read from the file
    SudokuBoard board(puzzle);

    // Let's get started!
    cout << "PUZZLE:" << endl;
    cout << board << endl;

    if (solve(board)) {
        cout << "SOLUTION:" << endl;
        cout << board << endl;
    }
    else {
        cout << "Could not find a solution" << endl;
    }

    return 0;
}
