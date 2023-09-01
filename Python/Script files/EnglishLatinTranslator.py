'''Description: This program translates English text into Pig Latin. 
Pig Latin is a simple language game where you move the first letter 
of a word to the end and add "ay" or "yay" to the end, depending on 
whether the word starts with a vowel or consonant.'''

# Function to translate English to Pig Latin
def english_to_piglatin(english_text):
    words = english_text.split()  # Split the input text into words
    piglatin_words = []

    for word in words:
        if word[0].lower() in "aeiou":  # If the word starts with a vowel
            piglatin_word = word + "yay"
        else:
            # If the word starts with a consonant, move the consonant to the end and add "ay"
            piglatin_word = word[1:] + word[0] + "ay"
        
        piglatin_words.append(piglatin_word)

    return " ".join(piglatin_words)  # Join the translated words into a sentence

# Example usage
english_text = "Hello, how are you?"
piglatin_text = english_to_piglatin(english_text)
print("Original English:", english_text)
print("Pig Latin:", piglatin_text)
