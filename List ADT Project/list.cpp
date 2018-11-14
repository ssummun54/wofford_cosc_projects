//
// Created by Sergio A. Sum on 10/17/2017.
//

#include "list.h"

List::List() {
    _size = 0;
    _array_size = 2;
    _array_ptr = new int[2];
}

List::~List() {
    // Return the array to the heap
    delete[]_array_ptr;
}

int List::get_item_at(unsigned int index) const {
    return _array_ptr[index];
}

void List::set_item_at(unsigned int index, int item) {
    _array_ptr[index] = item;
}

unsigned int List::size() const {
    return _size;
}

void List::append(int item) {
    _adjust_array(); //make sure _size !=_array_size
    _array_ptr[_size] = item;
    ++_size;
}

int List::pop(unsigned int index) {
    int value = _array_ptr[index];
    for(int i = index; i < _size; ++i){
        _array_ptr[i] = _array_ptr[i+1];
    }
    --_size;
    return value;
}

void List::insert(unsigned int index, int item) {
    _adjust_array();
    for(int i = _size; i > index; --i){
        _array_ptr[i] = _array_ptr[i-1];
    }
    _array_ptr[index] = item;
    ++_size;
}

void List::sort(bool reverse){
    if (! reverse){
        for (int i = 1; i < _size; ++i){
            int key = _array_ptr[i];
            int j = i;
            while (j > 0 && _array_ptr[j - 1] > key){
                _array_ptr[j] = _array_ptr[j - 1];
                j--;
            }
            _array_ptr[j] = key;
        }
    }
    else{
        for (unsigned int i = 1; i < _size; ++i){
            int key = _array_ptr[i];
            int j = i;
            while (j > 0 && _array_ptr[j-1] < key){
                _array_ptr[j] = _array_ptr[j - 1];
                j--;
            }
            _array_ptr[j] = key;
        }
    }
    }
void List::_adjust_array() {
    if (_size == _array_size) {
        //We need a bigger array
        int *new_array_ptr = new int[2 * _array_size];

        //copy old array to new array
        for (int i = 0; i < _array_size; ++i) {
            new_array_ptr[i] = _array_ptr[i];
        }
        delete[]_array_ptr;
        _array_ptr = new_array_ptr;
        _array_size *= 2;
    }
}