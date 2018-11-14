#!/usr/bin/env python3
"""
This module defines two functions that sort lists.

Each function is called multiple times and the best running time is
displayed.

Sorted lists are randomly ordered. A different list is used each
trial, which might be an issue when comparing two algorithms.
"""

import timeit  # https://docs.python.org/3.5/library/timeit.html
from sorting import selection_sort, insertion_sort
import sys

__author__ = 'David Sykes'

# In the setup, N is the number of items to sort.
# while k is the name of the function--e.g., insertion_sort.
SETUP_TEMPLATES = {
    'random': '''# Generate a list
import random
from __main__ import {F} as sort_function
N = {N}
list_to_sort = list(range(N))
random.shuffle(list_to_sort)
''',
    'ordered': '''# Generate a list
import random
from __main__ import {F} as sort_function
N = {N}
list_to_sort = list(range(N))
''',
    'reversed': '''# Generate a list
import random
from __main__ import {F} as sort_function
N = {N}
list_to_sort = list(range(N))
list_to_sort.reverse()
'''
}


def time_sort(item_count, run_count, list_state, sort_fcn):
    """
    Time the call to a sort function, giving it a list of item_count
    values
    :param item_count: A positive int
    :param run_count: A positive int
    :param list_state: one of 'random', 'ordered', or 'reversed'
    :param sort_fcn: a sort function that has one parameter, a list
    :return: a 4-tuple,
             (sort_fcn name, item_count, minimum runtime, list_state)
    """

    # Select the script to time
    setup_template = SETUP_TEMPLATES[list_state]

    # Create a Timer object and then call the function 10000 times
    sort_fcn_name = sort_fcn.__name__
    timer = timeit.Timer(stmt='sort_function(list_to_sort)',
                         setup=setup_template.format(N=item_count, F=sort_fcn_name))

    # Time 100 calls to the function, repeating run_count times
    times = timer.repeat(run_count, 100)

    return sort_fcn_name, item_count, min(times), list_state


def main():
    if len(sys.argv) != 4:
        print('Usage: {} list-size trials {random|ordered|reversed}',
              file=sys.stderr)
        sys.exit(1)

    # Check the values of the command line args
    try:
        item_count = int(sys.argv[1])
    except ValueError:
        print('item-count must be an integer', file=sys.stderr)
        sys.exit(2)
    try:
        run_count = int(sys.argv[2])
    except ValueError:
        print('item-count must be an integer', file=sys.stderr)
        sys.exit(3)
    list_state = sys.argv[3]
    if list_state not in ('random', 'ordered', 'reversed'):
        print("Third arg must be one of 'random', 'ordered', or 'reversed'",
              file=sys.stderr)
        sys.exit(4)

    # Print report headings
    print(' Function      |  List   | run time (sec)   | Start')
    print(' Name          |  Length | [best of {:4}]   | State'.format(run_count))
    print('---------------+---------+------------------+--------')
    for fcn in (insertion_sort, selection_sort):
        # print('{:13} |{:8,d} |{:15.7f}   | {}'.format(fcn.__name__, item_count, min(times), list_state))
        print('{:13} |{:8,d} |{:15.7f}   | {}'.format(*time_sort(item_count, run_count, list_state, fcn)))


if __name__ == '__main__':
    main()