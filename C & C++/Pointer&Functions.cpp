#include <iostream>

void swap(int* a, int* b) {
    int temp = *a;
    *a = *b;
    *b = temp;
}

int main() {
    int x = 5, y = 10;

    std::cout << "Before swap: x = " << x << ", y = " << y << std::endl;
    swap(&x, &y); // Pass addresses of x and y to the swap function
    std::cout << "After swap: x = " << x << ", y = " << y << std::endl;

    return 0;
}
