"""
Functions to sort a list
"""

__author__ = "David Sykes"


def selection_sort(lst):
    """
    Rearrange the values in a list so they are sorted.

    :param lst: a list of values
    :return: None. The values in lst are rearranged so that they are sorted
    """
    n = len(lst)
    for i in range(n):
        # Find the index of the smallest item from index position i to
        # the end of lst
        j = i
        for k in range(i + 1, n):
            if lst[k] < lst[j]:
                j = k

        # Swap the two values at lst[i] and lst[j]
        lst[i], lst[j] = lst[j], lst[i]


def insertion_sort(lst):
    """
    Rearrange the values in a list so they are sorted.

    :param   lst: a list of values
    :return: None. The values in lst are rearranged so that
             they are sorted
    """
    n = len(lst)
    for i in range(1, n):
        key = lst[i]

        # Insert key into the sorted sequence L[0]..L[i - 1]
        j = i
        while j > 0 and lst[j - 1] > key:
            lst[j] = lst[j - 1]
            j -= 1
        lst[j] = key