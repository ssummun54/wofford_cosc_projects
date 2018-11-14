/*
 * The purpose of this program is to test the ADT
 * DoublyLinkedList
 */

#include <stdio.h>
#include <assert.h>

#include "doublylinkedlist.h"

void print_list(struct DoublyLinkedList *listPtr);


int main (int argc, const char * argv[]) {

    ValueType value[] = {10, 20, 30, 40, 50, 60, 70, 80};
    size_t n;
    n = sizeof value / sizeof(ValueType);

    printf("This program prints an empty list. Then it\n");
    printf("prints an operation and then a list. Make sure\n");
    printf("the list below an operation reflects correct\n");
    printf("completion of that operation.\n");
    putchar('\n');
    printf("This code does some checking. If you spot an\n");
    printf("assertion error, then the most recent operation\n");
    printf("failed.\n");
    putchar('\n');

    /* Set up a new list */
    struct DoublyLinkedList list;
    init_dll(&list);
    assert(size_dll(&list) == 0);
    print_list(&list);

    /* First check that append() works correctly */
    size_t i;
    size_t j;
    for (i = 0 ; i < n ; ++i) {
        printf("APPEND %d\n", value[i]);
        append_dll(&list, value[i]);
        print_list(&list);
        assert(contains_dll(&list, value[i]) == 1);
        assert(get_at_dll(&list, i) == value[i]);
        assert(size_dll(&list) == i + 1);

        /* Check that any previously appended values are still in place */
        for (j = 0; j < i; ++j) {
            assert(get_at_dll(&list, j) == value[j]);
        }
    }

    /* Check that the list contains all of the values and no extras */
    for (int i = 0; i < n; ++i) {
        int result = contains_dll(&list, value[i]);
        printf("CONTAINS %d -> %d\n", value[i],result);
        print_list(&list);
        assert(contains_dll(&list, value[i]) == 1);
    }
    printf("CONTAINS %d -> %d\n", 99, contains_dll(&list, 99));
    print_list(&list);
    assert(contains_dll(&list, value[i]) == 0);

    /* Set each item in the list to its double */
    for (int i = 0; i < n; ++i) {
        // int current_value = get_at_dll(&list, i);
        value[i] *= 2;
        printf("SET_AT INDEX %d TO %d\n", i, value[i]);
        set_at_dll(&list, i, value[i]);
        assert(get_at_dll(&list, i) == value[i]);
        print_list(&list);
    }

    /* Remove a value that is not in the list */
    printf("REMOVE 99\n");
    remove_dll(&list, 99);
    print_list(&list);
    assert(size_dll(&list) == n);

    /* Check that remove_dll() works correctly. */
    // Define the stream of index values to remove
    size_t index[] = {3, 6, 0, 4, 1, 2, 5, 7};
    for (i = 0; i < n; ++i) {
        printf("REMOVE %d\n", value[index[i]]);
        remove_dll(&list, value[index[i]]);
        print_list(&list);
        assert(size_dll(&list) == n - i - 1);
        assert(contains_dll(&list, value[index[i]]) == 0);
    }

    printf("FREE\n");
    free_dll(&list);
    printf("    Since the list has been destroyed, it cannot be printed.\n");
    printf("    Make sure your code calls free() for each node.");

    return 0;
}

void print_list(struct DoublyLinkedList *listPtr) {
    /* Print the list */
    size_t i;

    printf("[ ");
    for (i = 0; i < size_dll(listPtr); ++i) {
        printf("%d ", get_at_dll(listPtr, i));
    }
    printf("]\n");
}