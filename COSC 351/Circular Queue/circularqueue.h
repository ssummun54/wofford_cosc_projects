//
// Created by summu on 5/7/2018.
//

#ifndef CIRCULARQUEUE_H
#define CIRCULARQUEUE_H

#include <iostream>

using namespace std;

const unsigned int CAP = 100;

class QueueUnderflow : public std::exception {
public:
    QueueUnderflow() {
        std::exception();
    }
};


class QueueOverflow : public std::exception {
public:
    QueueOverflow() {
        std::exception();
    }
};

template<typename T, const unsigned int CAP>
class Queue{
    /*
     * A queue is a collection that organizes data according
     * to a FIFO ordering.
     */
public :

    Queue<T, CAP>();

    void enqueue(T value) throw (QueueOverflow);

    T dequeue() throw (QueueUnderflow);

    T peek(unsigned int k=0) const;

    unsigned int size() const;

    unsigned int capacity() const;

    bool is_empty() const;

    bool is_full() const;

private:
    /*
     * Use an array _array to hold values in the queue. The
     * array contains CAP elements. Keep track of the
     * current portion of the array being used using four
     * instance variables:
     *     - _size, the number of items in the queue
     *     - _front_index, the index such that _array[_front_index]
     *       holds the value at the fron of the queue (as long as
     *       _size > 0).
     *     - _back_index., the index such that _array[_back_index]
     *       holds the value at the back of the queue (as long as
     *       _size > 0).
     *
     * INVARIANTS:
     *  1. 0 <=  _size <= CAP
     *  2. _size > 0 --> _back_index == (_front_index + len(self)-1) % CAP)
     *  3. _size == 0 --> _front_index == (_back_index + 1) % CAP)
     *  4. _size > 0 --> _array[_front_index] holds the front value and _array[_back_index] holds
     *                   the back value
     */
    T _array[CAP];
    unsigned int _size;
    int _front_index;
    int _back_index;
};

template<typename T, const unsigned int CAP>
ostream &operator<<(ostream &os, const Queue<T, CAP> &queue);

template<typename T, const unsigned int CAP>
Queue<T, CAP>::Queue() :
        _size(0), _front_index(1), _back_index(0) {
}
template<typename T, const unsigned int CAP>
void Queue<T, CAP>::enqueue(T value) throw (QueueOverflow) {
    if (_size == CAP) {
        throw QueueOverflow();
    }
    _back_index = (_back_index + 1) % CAP;
    _array[_back_index] = value;
    ++_size;
}
template<typename T, const unsigned int CAP>
T Queue<T, CAP>::dequeue() throw (QueueUnderflow) {
    if (_size) {
        T front_value = _array[_front_index];
        _front_index = (_front_index + 1) % CAP;
        --_size;
        return front_value;
    }
    throw QueueUnderflow();
}
template<typename T, const unsigned int CAP>
T Queue<T, CAP>::peek(unsigned int k) const {
    return _array[(_front_index + k) % CAP];
}
template<typename T, const unsigned int CAP>
unsigned int Queue<T, CAP>::size() const {
    return _size;
}
template<typename T, const unsigned int CAP>
unsigned int Queue<T, CAP>::capacity() const {
    return CAP;
}
template<typename T, const unsigned int CAP>
bool Queue<T, CAP>::is_empty() const {
    return _size == 0;
}
template<typename T, const unsigned int CAP>
bool Queue<T, CAP>::is_full() const {
    return _size == CAP;
}

template<typename T, const unsigned int CAP>
ostream &operator<<(ostream &os, const Queue<T, CAP> &queue) {
    // Use peek() to access the values in the queue from back to front
    os << "-->[";
    for (unsigned int i = queue.size(); i > 1 ; --i) {
        os << queue.peek(i - 1)  << ' ';
    }
    os << queue.peek(0);
    os << "] -->";
    return os;
}


#endif