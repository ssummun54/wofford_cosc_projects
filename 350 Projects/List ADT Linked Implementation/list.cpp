//
// Created by Sergio A. Sum on 10/25/2017.
//


#include "list.h"
#include <utility>


List::List() {
    _size = 0;
    _head_node_ptr = nullptr;
    _tail_node_ptr = nullptr;
}

List::~List() {
    for( int i = 0; i < _size; ++i){
        pop(static_cast<unsigned int>(i));
    }

}

int List::get_item_at(unsigned int index) const {
    return _kth_node(index)->item;
}

void List::set_item_at(unsigned int index, int item) {
    struct ListNode *current_node = _kth_node(index);
    current_node->item = item;
}

unsigned int List::size() const {
    return _size;
}

void List::append(int item) {
    if (_size == 0) {
        struct ListNode *new_node_ptr = _new_node(item, nullptr);
        _head_node_ptr = new_node_ptr;
        _tail_node_ptr = _head_node_ptr;
    } else {
        struct ListNode *new_node_ptr = _new_node(item, nullptr);
        _tail_node_ptr->next_node_ptr = new_node_ptr;
        _tail_node_ptr = new_node_ptr;
    }

    _size++;
}

int List::pop(unsigned int index) {

    if (index == 0) {
        int value = _head_node_ptr->item;
        struct ListNode *node_ptr = _head_node_ptr->next_node_ptr;
        delete _head_node_ptr;
        _head_node_ptr = node_ptr;
        _size--;
        return value;
    } else if (index == _size - 1) {
        struct ListNode *prev_node_ptr = _kth_node(index - 1);
        struct ListNode *node_ptr = prev_node_ptr->next_node_ptr;
        prev_node_ptr->next_node_ptr = nullptr;
        int value = node_ptr->item;
        delete node_ptr;
        _tail_node_ptr = prev_node_ptr;
        _size--;
        return value;
    } else {
        struct ListNode *prev_node_ptr = _kth_node(index - 1);
        struct ListNode *node_ptr = prev_node_ptr->next_node_ptr;
        prev_node_ptr->next_node_ptr = node_ptr->next_node_ptr;
        int value = node_ptr->item;
        delete node_ptr;
        _size--;
        return value;
    }

}

void List::insert(unsigned int index, int item) {
    if ((_size == 0) || (index == _size)) {
        append(item);

    } else {
        if (index == int(0)) {
            struct ListNode *new_node_ptr = _new_node(item, _head_node_ptr);
            _head_node_ptr = new_node_ptr;
        } else {
            struct ListNode *previous_node_ptr = _kth_node(index - 1);
            struct ListNode *new_node_ptr = _new_node(item, previous_node_ptr->next_node_ptr);
            previous_node_ptr->next_node_ptr = new_node_ptr;
        }
        ++_size;
    }

}

void List::sort(bool reverse) {
    if (reverse) {
        for (struct ListNode *i_node_ptr = _head_node_ptr; i_node_ptr != nullptr; i_node_ptr = i_node_ptr->next_node_ptr) {
            struct ListNode *j_node_ptr = i_node_ptr;
            for (struct ListNode *k_node_ptr = i_node_ptr->next_node_ptr; k_node_ptr != nullptr; k_node_ptr = k_node_ptr->next_node_ptr) {
                if (k_node_ptr->item > j_node_ptr->item) {
                    j_node_ptr = k_node_ptr;
                }
            std::swap(i_node_ptr -> item, j_node_ptr -> item);
            }
        }

    }
    else{
        for (struct ListNode *i_node_ptr = _head_node_ptr; i_node_ptr != nullptr; i_node_ptr = i_node_ptr->next_node_ptr) {
            struct ListNode *j_node_ptr = i_node_ptr;
            for (struct ListNode *k_node_ptr = i_node_ptr->next_node_ptr; k_node_ptr != nullptr; k_node_ptr = k_node_ptr->next_node_ptr) {
                if (k_node_ptr->item < j_node_ptr->item) {
                    j_node_ptr = k_node_ptr;
                }

            }
            std::swap(i_node_ptr -> item, j_node_ptr -> item);
        }
    }
}

struct List::ListNode *List::_new_node(int item, struct ListNode *next_node_ptr) {
    auto *new_node_ptr = new struct ListNode;
    new_node_ptr->item = item;
    new_node_ptr->next_node_ptr = next_node_ptr;
    return new_node_ptr;
}

struct List::ListNode *List::_kth_node(unsigned int k) {
    if (k == 0) {
        return _head_node_ptr;
    } else {
        struct ListNode *current_node = _head_node_ptr;

        for (int i = k; i > 0; i--) {
            current_node = current_node->next_node_ptr;
        }

        return current_node;
    }
}

const struct List::ListNode *List::_kth_node(unsigned int k) const {
    if (k == 0) {
        return _head_node_ptr;
    } else {
        struct ListNode *current_node = _head_node_ptr;

        for (int i = k; i > 0; i--) {
            current_node = current_node->next_node_ptr;
        }

        return current_node;
    }
}