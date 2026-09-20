
import random

# List of 5 predefined words
words = ["python", "computer", "program", "coding", "developer"]

# Choose a random word
word = random.choice(words)

# Create blanks for the word
hidden_word = ["_"] * len(word)

# Game variables
wrong_guesses = 0
max_wrong_guesses = 6
guessed_letters = []

print("================================")
print("       HANGMAN GAME")
print("================================")
print("Guess the word one letter at a time!")
print("You have 6 wrong guesses allowed.")

# Main game loop
while wrong_guesses < max_wrong_guesses and "_" in hidden_word:

    print("\nWord:", " ".join(hidden_word))
    print("Wrong guesses:", wrong_guesses, "/", max_wrong_guesses)

    if guessed_letters:
        print("Guessed letters:", " ".join(guessed_letters))

    # Get player's guess
    guess = input("Enter a letter: ").lower()

    # Check input
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter only one letter.")
        continue

    # Check if already guessed
    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue

    # Store the guess
    guessed_letters.append(guess)

    # Check whether the guess is correct
    if guess in word:
        print("Correct! The letter is in the word.")

        # Reveal the guessed letter
        for i in range(len(word)):
            if word[i] == guess:
                hidden_word[i] = guess

    else:
        wrong_guesses += 1
        print("Wrong guess!")

# Game result
print("\n================================")

if "_" not in hidden_word:
    print("CONGRATULATIONS!")
    print("You guessed the word:", word)
else:
    print("GAME OVER!")
    print("The correct word was:", word)

print("================================")
