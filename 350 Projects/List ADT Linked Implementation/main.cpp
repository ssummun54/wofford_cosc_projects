#include <iostream>
#include <cstdlib>
#include <cassert>
using namespace std;

#include "list.h"

ostream &operator<<(ostream &os, const List &int_list);


int main (int argc, char * const argv[]) {

    // Retrieve the list values from the command line.
    // Check that at least three command-line arguments are provided,
    // the program name, the value to search for, and list values
    if (argc < 2) {
        cerr << "Usage: " << argv[0] << "<int> [<int>]..." << endl;
        cerr << "Enter list values as command line arguments." << endl;
        return 1;
    }

    List test_list;

    // Convert each command-line values to an int value and store it in array a
    unsigned int n = (unsigned int)argc - 1;
    int a[n];  // n array of n int values
    for (int k = 1 ; k < argc ; ++k) {
        a[k-1] = atoi(argv[k]);
    }

    // Cause stdout to be flushed after every << operation to help with debugging
    // http://stackoverflow.com/questions/6214629/stdout-and-need-to-flush-it-c
    std::cout.setf( std::ios_base::unitbuf );

    // Check append(), get_item_at(), and size()
    cout << "Check append(), get_item_at(), and size()" << endl;
    for (unsigned int k = 0; k < n; ++k) {
        assert(test_list.size() == k);
        cout << "After appending " << a[k] << ": " << flush;
        test_list.append(a[k]);
        cout << test_list << endl;
        assert(test_list.size() == k+1);
        for (unsigned int j = 0; j < test_list.size(); ++j) {
            assert(test_list.get_item_at(j) == a[j]);
        }
    }
    cout << endl;

    // Check pop(), get_item_at, and size() by popping half of the values randomly
    cout << "Check pop(), at, and size() by popping half of the values randomly" << endl;
    int popped_value;
    for (unsigned int k = n; k > n / 2; --k) {
        // Generate a random index
        int j = rand() % k;

        assert(test_list.get_item_at(j) == a[j]);
        cout << "After pop from index " << j << ": " << flush;
        popped_value = test_list.pop(j);
        cout << test_list << '(' << popped_value << " was popped)" << endl;
        assert(test_list.size() == k-1);
        copy(a+(j+1), a+k, a+j);
    }
    cout << endl;

    unsigned int k = test_list.size();
    cout << "After inserting the value 200 at index " << test_list.size() << ": " << flush;
    test_list.insert(test_list.size(), 200);
    cout << test_list << endl;
    assert(test_list.get_item_at(test_list.size() -  1) == 200);
    assert(test_list.size() == k + 1);

    cout << "After inserting the value 300 at index 0: " << flush;
    k = test_list.size();
    test_list.insert(0, 300);
    cout << test_list << endl;
    assert(test_list.get_item_at(0) == 300);
    assert(test_list.size() == k + 1);

    unsigned int m = test_list.size() / 2;
    k = test_list.size();
    cout << "After inserting the value 400 at index " << m << ": " << flush;
    test_list.insert(m, 400);
    cout << test_list << endl;
    assert(test_list.get_item_at(m) == 400);
    assert(test_list.size() == k + 1);

    cout << endl;

    cout << "Check set_item_at()" << endl;
    k = test_list.size();
    for (unsigned int i = 0; i < test_list.size(); ++i) {
        int item = test_list.get_item_at(i);
        cout << "set_item_at(" << i << ", " << item + 1 << ')' << endl;
        test_list.set_item_at(i, item + 1);
        cout << "The list is now " << test_list << endl;
        assert(test_list.get_item_at(i) == item + 1);
        assert(test_list.size() == k);  // no change
    }

    cout << "Sorting:" << endl;
    cout << "    Check that values are listed in ascending order" << endl;
    test_list.sort();
    cout << "    " << test_list << endl;
    assert(test_list.size() == k);  // no change
    cout << "    Check that values are listed in descending order" << endl;
    test_list.sort(true);
    cout << "    " << test_list << endl;
    assert(test_list.size() == k);  // no change

    return 0;
}

// A function that overloads the << operator for List objects
ostream &operator<<(ostream &os, const List &int_list) {
    if (int_list.size() == 0) {
        os << "[]";
    }
    else {
        os << '[' << int_list.get_item_at(0);
        for (unsigned int i = 1; i < int_list.size(); ++i) {
            os << ", " << int_list.get_item_at(i);
        }
        os << ']';
    }
    return os;
}
