import random

class WordGuessingGame:
    def __init__(self, word_bank):
        self.secret_word = random.choice(word_bank).lower()
        self.guesses_left = 5  # Number of letter guesses allowed
        self.word_guesses_left = 3  # Number of word guesses allowed

    def take_turn(self):
        print(f"Guess the word! You have {self.guesses_left} letter guesses and {self.word_guesses_left} word guesses left.")
        while self.guesses_left > 0 or self.word_guesses_left > 0:
            guess = input("Enter a letter or guess the whole word: ").lower()

            if len(guess) == 1:  # Assuming it's a letter guess
                if guess in self.secret_word:
                    occurrences = self.secret_word.count(guess)
                    print(f"Correct! The letter '{guess}' appears {occurrences} times.")
                else:
                    print("Incorrect!")
                self.guesses_left -= 1

            elif guess == self.secret_word:
                print("Congratulations! You guessed the word correctly!")
                return
            else:
                self.word_guesses_left -= 1
                if self.word_guesses_left == 0:
                    print(f"Game Over! You've used all your word guesses. The word was '{self.secret_word}'.")
                    return
                else:
                    print("Incorrect word guess. Try again!")

            print(f"You have {self.guesses_left} letter guesses and {self.word_guesses_left} word guesses left.")
            if self.guesses_left == 0:
                print(f"Sorry, you've run out of letter guesses. The word was: {self.secret_word}")
                return

# Main function
def main():
    word_bank = ["Nike", "Adidas", "Puma", "Lululemon", "Sketchers"]
    game = WordGuessingGame(word_bank)
    game.take_turn()

# Run the game
if __name__ == "__main__":
    main()
