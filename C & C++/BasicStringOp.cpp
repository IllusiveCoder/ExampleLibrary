#include <iostream>
#include <string>

    // This C++ program performs basic string operations on user input.
    // It takes a string as input from the user.
    // It calculates the length of the string and prints it.
    // It converts the string to uppercase and prints the result.
    // It reverses the string and prints the reversed string.

int main() {
    std::string input;
    std::cout << "Enter a string: ";
    std::getline(std::cin, input);

    // Find the length of the string
    int length = input.length();
    std::cout << "Length of the string: " << length << std::endl;

    // Convert to uppercase
    for (char &c : input) {
        c = std::toupper(c);
    }
    std::cout << "Uppercase: " << input << std::endl;

    // Reverse the string
    std::string reversed(input.rbegin(), input.rend());
    std::cout << "Reversed: " << reversed << std::endl;

    return 0;
}
