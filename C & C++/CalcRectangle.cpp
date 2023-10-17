#include <iostream>

    // This C++ program calculates the area of a rectangle.
    // It takes the length and width of the rectangle as user input.
    // The area is calculated by multiplying the length and width.
    // The program then prints the calculated area.

int main() {
    // Input
    double length, width;
    std::cout << "Enter the length of the rectangle: ";
    std::cin >> length;
    std::cout << "Enter the width of the rectangle: ";
    std::cin >> width;

    // Calculate area
    double area = length * width;

    // Output
    std::cout << "The area of the rectangle is: " << area << std::endl;

    return 0;
}
