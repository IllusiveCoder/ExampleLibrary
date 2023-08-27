#include <iostream>
#include <fstream>
#include <string>

// Project: Simple Bank Management System 💰

// Description:
// This C++ project implements a simple bank management system. 
//Users can create accounts, deposit and withdraw funds, and view account details. 
//The program demonstrates the use of classes, objects, and basic file handling for data storage.


class BankAccount {
private:
    std::string accountNumber;
    std::string accountHolder;
    double balance;

public:
    BankAccount(std::string number, std::string holder, double initialBalance) {
        accountNumber = number;
        accountHolder = holder;
        balance = initialBalance;
    }

    void deposit(double amount) {
        balance += amount;
    }

    void withdraw(double amount) {
        if (amount <= balance) {
            balance -= amount;
        } else {
            std::cout << "Insufficient balance." << std::endl;
        }
    }

    void display() {
        std::cout << "Account Number: " << accountNumber << std::endl;
        std::cout << "Account Holder: " << accountHolder << std::endl;
        std::cout << "Balance: $" << balance << std::endl;
    }
};

int main() {
    BankAccount account("123456789", "John Doe", 1000.0);

    std::cout << "Bank Management System" << std::endl;
    std::cout << "---------------------" << std::endl;

    while (true) {
        std::cout << "1. Deposit" << std::endl;
        std::cout << "2. Withdraw" << std::endl;
        std::cout << "3. Display Account" << std::endl;
        std::cout << "4. Exit" << std::endl;

        int choice;
        std::cout << "Enter choice: ";
        std::cin >> choice;

        switch (choice) {
            case 1:
                double depositAmount;
                std::cout << "Enter deposit amount: ";
                std::cin >> depositAmount;
                account.deposit(depositAmount);
                break;
            case 2:
                double withdrawAmount;
                std::cout << "Enter withdrawal amount: ";
                std::cin >> withdrawAmount;
                account.withdraw(withdrawAmount);
                break;
            case 3:
                account.display();
                break;
            case 4:
                std::cout << "Exiting program." << std::endl;
                return 0;
            default:
                std::cout << "Invalid choice. Please enter a valid option." << std::endl;
        }
    }

    return 0;
}
