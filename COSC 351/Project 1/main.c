#include <stdio.h>
#include <stdlib.h>

#define MAX_N 20000

int main(int argc, const char **argv) {
    int N = atoi(argv[1]);
    int sieve[MAX_N];

    // make the array from 2 to N
    for(int count = 0; count <= N-2; ++count) {
        sieve[count] = count + 2;
    }


    for(int i = 0; i<=N-2; ++i){
        // if the value at sieve[i] is not 0
        if(sieve[i] != 0){
            // find the value at sieve[i]
            int value = sieve[i];
            // find the index of the next multiple of value
            int j = i + value;
            // while the next index is less than the index that carries N
            while(j<N-2){
                // replace sieve[j] with 0 (cross out)
                sieve[j] = 0;
                // get the index of the next multiple
                j = j + value;

            }
        }
    }

    // print out all the prime numbers from 2 to N
    for (int i = 0; i<= N-2; ++i){
        if(sieve[i] != 0){
            printf("%d ", sieve[i]);
        }
    }

    printf("\n");

    return 0;
}