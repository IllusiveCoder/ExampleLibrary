#include <iostream>

bool isPrime(int number) {
    if (number <= 1) {
        return false; // 0 and 1 are not prime numbers
    }
    
    for (int i = 2; i * i <= number; i++) {
        if (number % i == 0) {
            return false; // Found a divisor, not a prime number
        }
    }
    
    return true; // No divisors found, it's a prime number
}

int main() {
    int n;
    std::cout << "Enter a number: ";
    std::cin >> n;
    
    if (isPrime(n)) {
        std::cout << n << " is a prime number." << std::endl;
    } else {
        std::cout << n << " is not a prime number." << std::endl;
    }
    
    return 0;
}
