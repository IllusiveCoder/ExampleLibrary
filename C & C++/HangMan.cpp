#include <iostream>
#include <string>
#include <vector>
#include <ctime>
#include <cstdlib>

// Project: Hangman Game 🎮

// Description:
// This C++ project brings the classic Hangman game to life. 
// Players attempt to guess a hidden word by suggesting 
// letters one at a time. The program provides a limited 
// number of incorrect guesses before the hangman figure is 
// completed. It showcases basic string manipulation and 
// conditional logic.

const std::vector<std::string> words = {"apple", "banana", "cherry", "grape", "orange"};

std::string chooseRandomWord() {
    std::srand(static_cast<unsigned int>(std::time(nullptr)));
    int randomIndex = std::rand() % words.size();
    return words[randomIndex];
}

int main() {
    std::string secretWord = chooseRandomWord();
    std::string guessedLetters;
    int attemptsLeft = 6;

    std::cout << "Hangman Game" << std::endl;
    std::cout << "------------" << std::endl;

    while (attemptsLeft > 0) {
        std::cout << "Secret Word: ";
        for (char letter : secretWord) {
            if (guessedLetters.find(letter) != std::string::npos) {
                std::cout << letter << " ";
            } else {
                std::cout << "_ ";
            }
        }
        std::cout << std::endl;

        if (secretWord == guessedLetters) {
            std::cout << "Congratulations! You guessed the word: " << secretWord << std::endl;
            break;
        }

        std::cout << "Attempts left: " << attemptsLeft << std::endl;
        std::cout << "Guess a letter: ";
        char guess;
        std::cin >> guess;

        if (guessedLetters.find(guess) == std::string::npos) {
            guessedLetters += guess;
            if (secretWord.find(guess) == std::string::npos) {
                attemptsLeft--;
            }
        } else {
            std::cout << "You already guessed that letter." << std::endl;
        }
    }

    if (attemptsLeft == 0) {
        std::cout << "Sorry, you're out of attempts. The secret word was: " << secretWord << std::endl;
    }

    return 0;
}
