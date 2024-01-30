#include <iostream>

#define SIZE_LIMIT 100

class MyQueue {
private:
    // Define queue object. We use an array, a pointer towards our last index, and an
    // integer to define the current size.
    int* arr;
    int last_index;
    int size;
public:
    MyQueue() {
        // Constructor.
        this->arr = (int*) std::malloc(SIZE_LIMIT * sizeof(int));
        this->last_index = 0;
        this->size = 0;
    }
    
    void push(int x) {
        // Push an element to the final position and increase
        // both the last index and the size.
        this->arr[this->last_index++] = x;
        this->size++;
    }
    
    int pop() {
        // Obtain the element at the front of the
        // queue, remove it, and shift everything to the left.
        // Note that we decrease the last index and also the size.
        int front = this->arr[0];
        for (int i = 0; i < this->last_index - 1; i++) {
            this->arr[i] = this->arr[i + 1];
        }
        this->arr[this->last_index - 1] = 0;
        this->last_index--;
        this->size--;
        return front;
    }
    
    int peek() {
        // Constant time retrieval of first element.
        return this->arr[0];
    }
    
    bool empty() {
        // Constant time check to determine if array is empty.
        return this->size == 0;
    }
};