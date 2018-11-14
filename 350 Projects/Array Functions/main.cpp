#include <iostream>
#include <cstdlib>

using namespace std;

#include "arrayfunctions.h"

const int MAX_N = 100;

void print_array(int a[], int n);
    // Print the elements of a, an array having n values

int main(int argc, char **argv) {
    int a[MAX_N + 3];  // array to hold command line values plus a few more

    // Process command line arguments
    if (argc < 2) {
        cerr << "Usage: " << argv[0] << "int-1, int-2, ..., intN" << endl;
        return 1;
    }
    if (argc > MAX_N) {
        cerr << "Too many values to process. Maximum is " << MAX_N << endl;
        return 2;
    }

    // Convert the command line arguments to int values and place in a.
    for (int i = 1; i<argc; ++i) {
        a[i - 1] = atoi(argv[i]);
    }

    int n = argc - 1;  // Number of values copied from command line int a

    // Display the values in the array
    cout << "Processing: ";
    print_array(a, n);
    cout << endl;
    cout << endl;

    // Check shuffle_array()
    cout << "Calling shuffle_array()." << endl;
    cout << "Verify the array below contains " << n << " shuffled values" << endl;
    shuffle_array(a, n);
    print_array(a, n);
    cout << endl;
    cout << endl;

    // Check sort_array()
    cout << "Calling sort_array()." << endl;
    cout << "Verify the array below contains " << n << " sorted values" << endl;
    sort_array(a, n);
    print_array(a, n);
    cout << endl;
    cout << endl;

    // Check find_in_array()
    cout << "Calling find_in_array()." << endl;
    cout << "    Check first that values can be found..." << endl;
    int index[3] = {0, n / 2, n - 1};
    int val;
    int k;
    for (int i = 0; i < 3; ++i) {
        val = a[index[i]];
        k = find_in_array(val, a, n);
        if (k == index[i]) {
            cout << "       " << val << " found at " << k << "(correct)" << endl;
        } else {
            cout << "       " << val << " found at " << k << "(INCORRECT)" << endl;
        }
    }
    cout << "Enter a value NOT in the array: ";
    cin >> val;
    k = find_in_array(val, a, n);
    if (k == -1) {
        cout << "       " << val << " found at -1 (correct)" << endl;
    } else {
        cout << "       " << val << " found at " << k << "(INCORRECT)" << endl;
    }
    cout << endl;

    // Check insert_value_at()
    cout << "Calling insert_value_at()." << endl;
    insert_value_at(0, -1000, a, n);
    cout << "    Verify that -1000 is at index " << 0 << endl;
    ++n;
    cout << "        ";
    print_array(a, n);
    cout << endl;
    insert_value_at(n, 1000, a, n);
    cout << "    Verify that 1000 is at index " << n << endl;
    ++n;
    cout << "        ";
    print_array(a, n);
    cout << endl;
    insert_value_at(n / 2, 0, a, n);
    cout << "    Verify that 0 is at index " << n / 2 << endl;
    ++n;
    cout << "        ";
    print_array(a, n);
    cout << endl;
    cout << endl;

    // Check delete_value_at()
    cout << "Calling delete_value_at()." << endl;
    delete_value_at(n - 1, a, n);
    cout << "    Verify that 1000 at index " << (n - 1) << " was deleted" << endl;
    --n;
    cout << "        ";
    print_array(a, n);
    cout << endl;
    delete_value_at(n / 2, a, n);
    cout << "    Verify that 0 at index " << n / 2 << " was deleted" << endl;
    --n;
    cout << "        ";
    print_array(a, n);
    cout << endl;
    delete_value_at(0, a, n);
    cout << "    Verify that -1000 at index 0 was deleted" << endl;
    --n;
    cout << "        ";
    print_array(a, n);
    cout << endl;
    cout << endl;


    // Finally, check clear_array()
    cout << "Calling clear_array()." << endl;
    cout << "Verify the array below contains " << n << " zero values" << endl;
    clear_array(a, n);
    print_array(a, n);
    cout << endl;


    return 0;
}

void print_array(int a[], int n) {
    cout << '[';
    if (n) {
        cout << a[0];
        for (int i = 1; i < n; ++i) {
            cout << ", " << a[i];
        }
    }
    cout << ']';
}
