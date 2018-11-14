/*
 * The purpose of this program is to test the ADT IntList
 */

#include <iostream>
#include <iomanip>
#include <cassert>

using namespace std;

#include "intlist.h"


int main (int argc, const char * argv[]) {

    ValueType value[] = {10, 20, 30, 40, 50, 60, 70, 80};
    size_t n;
    n = sizeof value / sizeof(ValueType);

    cout << "This program prints an empty list. Then it" << endl;
    cout << "prints an operation and then a list. Make sure" << endl;
    cout << "the list below an operation reflects correct" << endl;
    cout << "completion of that operation." << endl;
    cout << endl;
    cout << "This code does some checking. If you spot an" << endl;
    cout << "assertion error, then the most recent operation" << endl;
    cout << "failed." << endl;
    cout << endl;

    cout << boolalpha;   // Display bool values as "true" or "false".

    /* Set up a new list */
    IntList list;

    assert(list.size() == 0);
    cout << list << endl;

    /* First check that append() works correctly */
    size_t i;
    size_t j;
    for (i = 0 ; i < n ; ++i) {
        cout << "APPEND " << value[i] << endl;
        list.append(value[i]);
        cout << list << endl;
        assert(list.contains(value[i]) == 1);
        assert(list[i] == value[i]);
        assert(list.size() == i + 1);

        /* Check that any previously appended values are still in place */
        for (j = 0; j < i; ++j) {
            assert(list[j] == value[j]);
        }
    }

    /* Check that the list contains all of the values and no extras */
    for (int i = 0; i < n; ++i) {
        bool result = list.contains(value[i]);
        cout << "CONTAINS " << value[i] << " --> " << result << endl;
        cout << list << endl;
        assert(list.contains(value[i]) == 1);
    }
    cout << "CONTAINS " << 99 << " --> " << list.contains(99) << endl;
    cout << list << endl;
    assert(list.contains(value[i]) == 0);

    /* Set each item in the list to its double */
    for (int i = 0; i < n; ++i) {
        // int current_value = list[i];
        value[i] *= 2;
        cout << "SET_AT INDEX " << i << " TO " << value[i] << endl;
        list[i] = value[i];
        assert(list[i] == value[i]);
        cout << list << endl;
    }

    /* Remove a value that is not in the list */
    cout << "REMOVE 99" << endl;
    list.remove(99);
    cout << list << endl;
    assert(list.size() == n);

    /* Check that remove_dll() works correctly. */
    // Define the stream of index values to remove
    size_t index[] = {3, 6, 0, 4, 1, 2, 5, 7};
    for (i = 0; i < n; ++i) {
        cout << "REMOVE " << value[index[i]] << endl;
        list.remove(value[index[i]]);
        cout << list << endl;
        assert(list.size() == n - i - 1);
        assert(list.contains(value[index[i]]) == 0);
    }

    cout << "    The destructor will run now." << endl;
    cout << "    Make sure your code deletes each node." << endl;

    return 0;
}