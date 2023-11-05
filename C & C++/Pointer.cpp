#include <iostream>

// Explanation:
//     We declare an integer array numbers and a pointer p to an integer.
//     The pointer p is initialized to point to the first element of the array.
//     Using a loop, we iterate through the elements of the array using pointer arithmetic.
//     *p is used to access the value pointed to by p, and p++ increments the pointer to the next element.

int main() {
    int numbers[] = {1, 2, 3, 4, 5};
    int* p = numbers; // Initialize a pointer to the start of the array

    for (int i = 0; i < 5; i++) {
        std::cout << "Element " << i << ": " << *p << std::endl; // Use * to access the value pointed to by p
        p++; // Move the pointer to the next element
    }

    return 0;
}
