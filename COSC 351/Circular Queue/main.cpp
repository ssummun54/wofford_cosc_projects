#include <iostream>
#include "circularqueue.h"


int main() {

    Queue<int, 20> int_queue;
    Queue<string, 10> string_queue;
    Queue<double, 20> double_queue;
    Queue<char, 26> char_queue;
    Queue<Queue<char, 26>, 10 > char_queue_queue;

    int_queue.enqueue(10);
    string_queue.enqueue("abcde");
    string_queue.enqueue("fghijklmn");
    string_queue.enqueue("opqrstuvwxyz");
    double_queue.enqueue(2.5);
    char_queue.enqueue('A');
    char_queue.enqueue('B');
    char_queue_queue.enqueue(char_queue);

    cout << "int_queue:    " << int_queue << endl;
    cout << "string_queue: " << string_queue << endl;
    cout << "char_queue: " << char_queue << endl;

    return 0;
}