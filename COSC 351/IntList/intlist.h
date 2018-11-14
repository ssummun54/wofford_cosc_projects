//
// Created by summu on 3/30/2018.
//
#ifndef INTLIST_ADT_INTLIST_H
#define INTLIST_ADT_INTLIST_H

#include <iostream>

typedef int ValueType;


class IntList {
public:

    IntList(void);

    ~IntList(void);

    size_t size(void) const;

    void append(const ValueType &value);

    bool contains(const ValueType &value);

    void remove(const ValueType &value);

    ValueType &operator[](size_t i);

    const ValueType &operator[](size_t i) const;

private:

    struct DoublyLinkedListNode {
        ValueType value;
        struct DoublyLinkedListNode *prev_node_ptr;
        struct DoublyLinkedListNode *next_node_ptr;
    };

    struct DoublyLinkedListNode *_dummy_head_node_ptr;
    size_t _size;

    struct DoublyLinkedListNode *get_node_at(size_t i);
    const struct DoublyLinkedListNode *get_node_at(size_t i) const;

    struct DoublyLinkedListNode *new_node_ptr(struct DoublyLinkedListNode *prev_node_ptr,
                                              ValueType value,
                                              struct DoublyLinkedListNode *next_node_ptr);
};

std::ostream &operator<<(std::ostream &os, const IntList &int_list);

#endif //INTLIST_ADT_INTLIST_H
