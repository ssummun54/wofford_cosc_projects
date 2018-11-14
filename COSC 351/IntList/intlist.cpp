//
// Created by summu on 3/30/2018.
//



#include "intlist.h"



IntList::IntList(void) {
    // Allocate and initialize the dummy head node.
    // We don't need to set a value in that node.
    struct DoublyLinkedListNode *new_node_ptr = new struct DoublyLinkedListNode;
    new_node_ptr->prev_node_ptr = new_node_ptr;
    new_node_ptr->next_node_ptr = new_node_ptr;

    // Set the dummy head node pointer and the size
    this->_dummy_head_node_ptr = new_node_ptr;
    this->_size = 0;
}

//free
IntList::~IntList(void) {
    struct DoublyLinkedListNode *dummy_head_node_ptr;
    struct DoublyLinkedListNode *current_node_ptr = this->_dummy_head_node_ptr->prev_node_ptr;
    for(int j = _size; j > 0; j--){
        current_node_ptr = current_node_ptr->next_node_ptr;
        free(current_node_ptr);
    }
    free(current_node_ptr);
}

size_t IntList::size(void) const{
    return _size;
}



void IntList::append(const ValueType &value) {
    struct DoublyLinkedListNode *last_node_ptr = this->_dummy_head_node_ptr->prev_node_ptr;
    struct DoublyLinkedListNode *new_node = new_node_ptr(last_node_ptr, value, this->_dummy_head_node_ptr);
    this->_dummy_head_node_ptr->prev_node_ptr = new_node;
    last_node_ptr->next_node_ptr = new_node;
    this ->_size++;
}

bool IntList::contains(const ValueType &value) {
    struct DoublyLinkedListNode *curr_node_ptr = this->_dummy_head_node_ptr;

    for (int j = 0; j< size(); j++){
        curr_node_ptr = curr_node_ptr->next_node_ptr;
        if(curr_node_ptr-> value == value){
            return 1;
        }
    }
    return 0;
}

void IntList::remove(const ValueType &value) {
    struct DoublyLinkedListNode *curr_node_ptr = this->_dummy_head_node_ptr;

    for (int j = 0; j< size(); j++) {
        curr_node_ptr = curr_node_ptr->next_node_ptr;
        if (curr_node_ptr->value == value) {
            curr_node_ptr -> prev_node_ptr -> next_node_ptr = curr_node_ptr->next_node_ptr;
            curr_node_ptr -> next_node_ptr-> prev_node_ptr = curr_node_ptr-> prev_node_ptr;
            struct DoublyLinkedListNode *temp_node_ptr = curr_node_ptr;
            curr_node_ptr = curr_node_ptr-> prev_node_ptr;
            free(temp_node_ptr);
            _size--;
        }
    }
}

ValueType &IntList::operator[](size_t i) {
    return get_node_at(i)->value;
}

const ValueType &IntList::operator[](size_t i) const {
    return this->get_node_at(i)->value;
}


struct IntList ::DoublyLinkedListNode * IntList::get_node_at(size_t i) {
    struct DoublyLinkedListNode *curr_node_ptr;
    curr_node_ptr = this->_dummy_head_node_ptr->next_node_ptr;
    for (size_t j = 0; j < i; ++j) {
        curr_node_ptr = curr_node_ptr->next_node_ptr;
    }
    return curr_node_ptr;
}

const struct IntList ::DoublyLinkedListNode * IntList::get_node_at(size_t i) const {
    struct DoublyLinkedListNode *curr_node_ptr;
    curr_node_ptr = this->_dummy_head_node_ptr->next_node_ptr;
    for (size_t j = 0; j < i; ++j) {
        curr_node_ptr = curr_node_ptr->next_node_ptr;
    }
    return curr_node_ptr;
}


std::ostream &operator<<(std::ostream &os, const IntList &int_list) {    /* Print the list */
    size_t i;

    os << "[ ";
    for (i = 0; i < int_list.size(); ++i) {
        os << int_list[i] << ' ';
    }
    os << "]" << std::endl;
    return os;
}

struct IntList::DoublyLinkedListNode *IntList::new_node_ptr(struct DoublyLinkedListNode *prev_node_ptr,
                                          ValueType value,
                                          struct DoublyLinkedListNode *next_node_ptr){
    struct DoublyLinkedListNode *new_node_ptr = new struct DoublyLinkedListNode;
    new_node_ptr->prev_node_ptr = prev_node_ptr;
    new_node_ptr->value = value;
    new_node_ptr-> next_node_ptr = next_node_ptr;

    return new_node_ptr;
}
