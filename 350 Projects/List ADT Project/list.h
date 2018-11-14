//
// Created by Sykes, David A on 10/12/17.
// Modified 2017-10-19. Made __aray_size unsigned int.
//

#ifndef LIST_ADT_ARRAY_IMPLEMENTATION_LIST_H
#define LIST_ADT_ARRAY_IMPLEMENTATION_LIST_H

class List {
public:
    List();
        /*
         * Construct an empty list
         */

    ~List();
        /*
         * Destructor
         */

    int get_item_at(unsigned int index) const;
        /*
         * Return the value in this list at an index.
         * Pre: 0 <= index < size()
         */

    void set_item_at(unsigned int index, int item);
        /*
         * Set the value in this list at an index to item.
         * Pre: 0 <= index < size()
         */
    unsigned int size() const;
        /*
         * Return the length of this list.
         */
    void append(int item);
        /*
         * Append an item to this list.
         */

    int pop(unsigned int index);
        /*
         * Remove the item a given index and return it
         * Pre: 0 <= index < size()
         */

    void insert(unsigned int index, int item);
        /*
         * Insert an item in this list so that it is at
         * a given index position.
         * Pre: 0 <= index <= n
         */

    void sort(bool reverse=false);
        /*
         * Rearrange the items in this list so they are
         * ordered. If reverse is false, then the items
         * are put into non-decreasing order. If reverse
         * is true, the items are put in non-increasing
         * order.
         */

private:
    unsigned int _size;
    unsigned int _array_size;
    int *_array_ptr;

    void _adjust_array();
        /*
         * If _size == _array_size then set _array_ptr to
         * point to an array twice as long, copying all
         * values from the current array to the new array.
         */
};

#endif //LIST_ADT_ARRAY_IMPLEMENTATION_LIST_H
