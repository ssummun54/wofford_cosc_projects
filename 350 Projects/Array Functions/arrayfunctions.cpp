//
// Created by summu on 10/6/2017.
//

#include "arrayfunctions.h"
#include "stdio.h"
#include "stdlib.h"
#include "time.h"

void clear_array(int a[], int n) {
    for (int j = 0; j < n; j++){
        a[j]=0;
    }
}

void shuffle_array(int a[], int n) {
    // Use the rand() function in cstdlib to generate
    // a random number.
    // See http://www.cplusplus.com/reference/cstdlib/rand/
    for (int i = 0; i < n; ++i){
     int temp = 0;
        int j = rand() % n + 0;
        temp = a[i];
        a[i] = a[j];
        a[j] = temp;



    }


}

int find_in_array(int val, int a[], int n) {
    int i;
    for(i=0; i < n && a[i] != val; i++){
    }
    return i == n ? -1:i; 
}

void sort_array(int a[], int n) {
    for (int i = 1; i < n; ++i){
        int key = a[i];
        int j = i;
        while (j > 0 && a[j - 1] < key){
            a[j] = a[j - 1];
            j--;
        }
        a[j] = key;
    }
}

void delete_value_at(int i, int a[], int n) {
    for (int j = i; j < n; ++j){
        a[j] = a[j + 1];
    }
}

void insert_value_at(int i, int val, int a[], int n) {
    for (int j = n; j > i; --j) {
        a[j] = a[j - 1];
    }
    a[i] = val;

}