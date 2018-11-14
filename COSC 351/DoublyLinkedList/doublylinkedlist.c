//
// Created by summu on 3/5/2018.
//

#include <stdio.h>
#include "doublylinkedlist.h"

struct DoublyLinkedListNode {
    struct DoublyLinkedListNode *prev_node_ptr;
    ValueType value;
    struct DoublyLinkedListNode *next_node_ptr;
};

struct DoublyLinkedListNode *create_node_ptr(struct DoublyLinkedListNode *prev_node_ptr, struct DoublyLinkedListNode *next_node_ptr, ValueType value){
    struct DoublyLinkedListNode *new_node_ptr = malloc(sizeof(struct DoublyLinkedListNode));
    new_node_ptr-> prev_node_ptr = prev_node_ptr;
    new_node_ptr-> next_node_ptr = next_node_ptr;
    new_node_ptr -> value = value;
    return new_node_ptr;
}


/* Initialize a doubly-linked list */
void init_dll(struct DoublyLinkedList *list_ptr) {
    // Allocate and initialize the dummy head node.
    // We don't need to set a value in that node.
    struct DoublyLinkedListNode *new_node_ptr =
            malloc(sizeof(struct DoublyLinkedListNode));

    new_node_ptr->prev_node_ptr = new_node_ptr;
    new_node_ptr->next_node_ptr = new_node_ptr;

    // Set the dummy head node pointer and the size
    list_ptr->dummy_head_node_ptr = new_node_ptr;
    list_ptr->size = 0;
}


/* Free all the space used by the given list */
void free_dll(struct DoublyLinkedList *list_ptr){
    struct DoublyLinkedListNode *current_node_ptr = list_ptr->dummy_head_node_ptr->next_node_ptr;
    struct DoublyLinkedListNode *next_node_ptr = current_node_ptr->next_node_ptr;

    while (current_node_ptr != list_ptr->dummy_head_node_ptr) {
        free(current_node_ptr);
        current_node_ptr = next_node_ptr;
        next_node_ptr = current_node_ptr->next_node_ptr;
    }
    free(current_node_ptr);
}


/* Return the number of values in the given list */
size_t size_dll(struct DoublyLinkedList *list_ptr){
    return list_ptr-> size;
}


/* Append the given value to the end of the given list */
void append_dll(struct DoublyLinkedList *list_ptr, ValueType value){
    struct DoublyLinkedListNode *last_node_ptr = list_ptr->dummy_head_node_ptr->prev_node_ptr;
    struct DoublyLinkedListNode *new_node = create_node_ptr(last_node_ptr, list_ptr->dummy_head_node_ptr, value);
    list_ptr->dummy_head_node_ptr->prev_node_ptr = new_node;
    last_node_ptr->next_node_ptr = new_node;
    list_ptr ->size++;
}


/* Return 1 if the given value is in the given list, 0 otherwise */
int contains_dll(struct DoublyLinkedList *list_ptr, ValueType value){
    struct DoublyLinkedListNode *curr_node_ptr = list_ptr->dummy_head_node_ptr;

    for (int j = 0; j< size_dll(list_ptr); j++){
        curr_node_ptr = curr_node_ptr->next_node_ptr;
        if(curr_node_ptr-> value == value){
            return 1;
        }
    }
    return 0;
}


/* remove_dll the given value from the given list (if it is present) */
void remove_dll(struct DoublyLinkedList *list_ptr, ValueType value){
    struct DoublyLinkedListNode *curr_node_ptr = list_ptr->dummy_head_node_ptr;

    for (int j = 0; j< size_dll(list_ptr); j++) {
        curr_node_ptr = curr_node_ptr->next_node_ptr;
        if (curr_node_ptr->value == value) {
            curr_node_ptr -> prev_node_ptr -> next_node_ptr = curr_node_ptr->next_node_ptr;
            curr_node_ptr -> next_node_ptr-> prev_node_ptr = curr_node_ptr-> prev_node_ptr;
            struct DoublyLinkedListNode *temp_node_ptr = curr_node_ptr;
            curr_node_ptr = curr_node_ptr-> prev_node_ptr;
            free(temp_node_ptr);
            list_ptr->size--;
        }
    }
}

/* Return the value stored in the given list at the given offset i.
 * Precondition: 0 <= i < size_dll(list_ptr)
 */
ValueType get_at_dll(struct DoublyLinkedList *list_ptr, size_t i){
        struct DoublyLinkedListNode *curr_node_ptr;
        curr_node_ptr = list_ptr->dummy_head_node_ptr->next_node_ptr;
        for (size_t j = 0; j < i; ++j) {
            curr_node_ptr = curr_node_ptr->next_node_ptr;
        }
        return curr_node_ptr->value;
    }

/* Set the value stored in the given list at the given offset i to value.
 * Precondition: 0 <= i < size_dll(list_ptr)
 */
void set_at_dll(struct DoublyLinkedList *list_ptr, size_t i, ValueType value){
    struct DoublyLinkedListNode *curr_node_ptr;
    curr_node_ptr = list_ptr->dummy_head_node_ptr->next_node_ptr;
    for (size_t j = 0; j < i; ++j) {
        curr_node_ptr = curr_node_ptr->next_node_ptr;
    }
    curr_node_ptr->value = value;
}

