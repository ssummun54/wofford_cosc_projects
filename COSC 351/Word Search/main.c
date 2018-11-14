#include <stdio.h>
#include <ctype.h>
#include <memory.h>

#define MAX 100

typedef char Grid[MAX + 1][MAX + 1];

enum Direction {N, NE, E, SE, S, SW, W, NW };

struct GridLocation{
    int row;
    int col;
    enum Direction dir;
};

struct GridLocation find_word(Grid grid, char words[MAX+1], int n){
    struct GridLocation location;
    int k;
    int length = strlen(words);


    //north
    for(int col = n-1; col >= 0; --col){
        for(int row = n-1; row >= 0; --row){
            if(words[0] == grid[row][col] && length <= row){
                for(k = 1; k < length && words[k] == grid[row-k][col]; k++){

                }
                if(k == length){
                    location.row = row;
                    location.col = col;
                    location.dir = N;

                    return location;
                }
            }

        }
    }
    //northeast
    for(int row = 0; row < n; ++row){
        for(int col = 0; col < n; ++col){
            if(words[0] == grid[row][col] && n - col >= length && length <= row){
                for(k = 1; k < length && words[k] == grid[row - k][col + k]; k++){

                }
                if(k == length){
                    location.row = row;
                    location.col = col;
                    location.dir = NE;

                    return location;
                }
            }

        }
    }
    //east
    for(int row = 0; row < n; ++row){
        for(int col = 0; col < n; ++col){
            if(words[0] == grid[row][col] && n - col >= length){
                for(k = 1; k < length && words[k] == grid[row][col+k]; k++){

                }
                if(k == length){
                    location.row = row;
                    location.col = col;
                    location.dir = E;

                    return location;
                }
            }

        }
    }
    //southeast
    for(int col = 0; col < n; ++col){
        for(int row = 0; row < n; ++row){
            if(words[0] == grid[row][col] && n - col >= length && n - row >= length){
                for(k = 1; k < length && words[k] == grid[row + k][col+k]; k++){

                }
                if(k == length){
                    location.row = row;
                    location.col = col;
                    location.dir = SE;

                    return location;
                }
            }

        }
    }
    // south
    for(int col = 0; col < n; ++col){
        for(int row = 0; row < n; ++row){
            if(words[0] == grid[row][col] && n - row >= length){
                for(k = 1; k < length && words[k] == grid[row+k][col]; k++){

                }
                if(k == length){
                    location.row = row;
                    location.col = col;
                    location.dir = S;

                    return location;
                }
            }

        }
    }
    // southwest
    for(int col = 0; col < n; ++col){
        for(int row = 0; row < n; ++row){
            if(words[0] == grid[row][col] && col >= length - 1 && n - row >= length){
                for(k = 1; k < length && words[k] == grid[row + k][col-k]; k++){

                }
                if(k == length){
                    location.row = row;
                    location.col = col;
                    location.dir = SW;

                    return location;
                }
            }

        }
    }
    // west
    for(int row = 0; row < n; ++row){
        for(int col = 0; col < n; ++col){
            if(words[0] == grid[row][col] && col >= length - 1){
                for(k = 1; k < length && words[k] == grid[row][col-k]; k++){

                }
                if(k == length){
                    location.row = row;
                    location.col = col;
                    location.dir = W;

                    return location;
                }
            }

        }
    }



    //northwest
    for(int col = 0; col < n; ++col){
        for(int row = 0; row < n; ++row){
            if(words[0] == grid[row][col] && col >= length - 1 && length <= row){
                for(k = 1; k < length && words[k] == grid[row - k][col - k]; k++){

                }
                if(k == length){
                    location.row = row;
                    location.col = col;
                    location.dir = NW;

                    return location;
                }
            }

        }
    }
    return location;
}

int main(int argc, const char **argv) {
    struct GridLocation loc;

    const char * DIR_STR[8]={
            "NORTH", "NORTHEAST", "EAST", "SOUTHEAST", "SOUTH", "SOUTHWEST", "WEST", "NORTHWEST"
    };

    int n;
    // open file
    FILE *puzzle_file_ptr = fopen(argv[1], "r");

    // file can't be opened
    if(! puzzle_file_ptr){
        fprintf(stderr, "problem with %s.\n", argv[1]);
        return 1;
    }

    //only worry about the n x n part of the grid
    fscanf(puzzle_file_ptr, "%d", &n);

    char grid [MAX][MAX + 1];

    // fill in grid
    for(int i = 0; i<n; ++i){
        fscanf(puzzle_file_ptr, "%s", grid[i]);
    }

    // get words to be searched for and start searching

    char words[MAX + 1];

    while(fscanf(puzzle_file_ptr, "%s", words) != EOF){
        int i = 0;
        while(words[i]){
            words[i] = toupper(words[i]);
            ++i;
        }
        loc = find_word(grid, words, n);
        printf("%s", words);
        printf(" %d,%d %s \n", loc.row, loc.col, DIR_STR[loc.dir]);

    }

    return 0;
}