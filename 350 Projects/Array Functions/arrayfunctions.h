//
// Created by summu on 10/6/2017.
//

#ifndef ARRAY_FUNCTIONS_ARRAYFUNCTIONS_H
#define ARRAY_FUNCTIONS_ARRAYFUNCTIONS_H

void clear_array(int a[], int n);
    // Set all of the elements of a, an array having n
    // elements to zero.

void shuffle_array(int a[], int n);
    // Rearrange the values in a, an array having n
    // elements.

int find_in_array(int val, int a[], int n);
    // Search a, an array having n elements, for a
    // value val. If found, return the lowest index i
    // such that a[i] == val. Otherwise return -1.

void sort_array(int a[], int n);
    // Rearrange the values in a, an array of n
    // elements, such that a[i] <= a[i+1] for all
    // values of i in the range 0..(n-1).

void delete_value_at(int i, int a[], int n);
    // Precondition: 0 <= m < n.
    // Set a[j] = a[j + 1] for j = i..(n-1).

void insert_value_at(int i, int val, int a[], int n);
    // Precondition: 0 <= i < n.
    // Set a[j] = a[j-1] for j = n..i+1 and
    // then set a[i] = val.


#endif //ARRAY_FUNCTIONS_ARRAYFUNCTIONS_H
