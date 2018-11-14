//
// Created by summu on 10/25/2017.
//

#ifndef LISTADT_LINKEDIMPLEMENTATION_LIST_H
#define LISTADT_LINKEDIMPLEMENTATION_LIST_H

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

    struct ListNode {
        int item;
        struct ListNode *next_node_ptr;
    };

    unsigned int _size;
    struct ListNode *_head_node_ptr;
    struct ListNode *_tail_node_ptr;

    struct ListNode *_new_node(int item, struct ListNode *next_node_ptr);

    struct ListNode *_kth_node(unsigned int k);
    /*
     * Return the kth node in the chain
     */

    const struct ListNode *_kth_node(unsigned int k) const;
    /*
     * Return the kth node in the chain
     */
};
#endif //LISTADT_LINKEDIMPLEMENTATION_LIST_H
