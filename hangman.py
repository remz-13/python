import random
import os
import platform
import sys
import time

words = ['python', 'computer', 'hangman', 'programming', 'algorithm']

def choose_word():
    return random.choice(words)

def display_word(word, guessed_letters):
    return ' '.join([letter if letter in guessed_letters else '_' for letter in word])

def restart_computer():
    system_platform = platform.system()
    try:
        if system_platform == "Windows":
            os.system("shutdown /s")
        elif system_platform == "Linux" or system_platform == "Darwin":
            os.system("sudo reboot")
        else:
            print(f"Unsupported operating system: {system_platform}")
    except Exception as e:
        print(f"An error occurred: {e}")

def hangman():
    word = choose_word()
    guessed_letters = set()
    attempts = 6  

    print("Hangman")
    print(f"The word has {len(word)} letters.")

    while attempts > 0:
        print(display_word(word, guessed_letters))
        print(f"Attempts remaining: {attempts}")
        
        guess = input("Guess a letter: ").lower()

        if guess in guessed_letters:
            print("You already guessed that letter!")
            continue

        guessed_letters.add(guess)

        if guess in word:
            print(f"Good guess! {guess} is in the word.")
        else:
            attempts -= 1
            print(f"Wrong guess! {guess} is not in the word.")

        if all(letter in guessed_letters for letter in word):
            print(f"Congratulations, you guessed the word: {word}!")
            time.sleep(2)
            sys.exit()
            break
    else:
        restart_computer()

if __name__ == "__main__":
    hangman()
