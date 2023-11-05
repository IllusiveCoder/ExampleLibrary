#include <iostream>

// Explanation:

//     We allocate memory for an integer on the heap using the new operator.
//     We assign a value to the dynamically allocated integer using *dynamicInt.
//     After using the memory, it's crucial to release it with the delete operator to prevent memory leaks.

int main() {
    int* dynamicInt = new int; // Allocate memory for an integer on the heap
    *dynamicInt = 42; // Assign a value to the dynamically allocated integer

    std::cout << "Dynamically allocated integer: " << *dynamicInt << std::endl;

    delete dynamicInt; // Release the allocated memory

    return 0;
}
