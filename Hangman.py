import random

WORDS = ["python", "hangman", "computer", "keyboard", "programming"]

HANGMAN_STAGES = [
    """
       -----
       |   |
           |
           |
           |
           |
    =========""",
    """
       -----
       |   |
       O   |
           |
           |
           |
    =========""",
    """
       -----
       |   |
       O   |
       |   |
           |
           |
    =========""",
    """
       -----
       |   |
       O   |
      /|   |
           |
           |
    =========""",
    """
       -----
       |   |
       O   |
      /|\\  |
           |
           |
    =========""",
    """
       -----
       |   |
       O   |
      /|\\  |
      /    |
           |
    =========""",
    """
       -----
       |   |
       O   |
      /|\\  |
      / \\  |
           |
    =========""",
]

def display_board(wrong_guesses, guessed_letters, word):
    """Print the current hangman stage, guessed letters, and word progress."""
    print(HANGMAN_STAGES[wrong_guesses])
    print(f"\n  Wrong guesses left : {6 - wrong_guesses}")
    print(f"  Letters guessed    : {', '.join(sorted(guessed_letters)) or 'None'}")

    display_word = " ".join(letter if letter in guessed_letters else "_" for letter in word)
    print(f"\n  Word: {display_word}\n")


def get_player_guess(guessed_letters):
    """Ask the player for a valid, single, not-yet-guessed letter."""
    while True:
        guess = input("  Guess a letter: ").lower().strip()
        if len(guess) != 1:
            print("  ⚠  Please enter exactly ONE letter.")
        elif not guess.isalpha():
            print("  ⚠  Please enter a LETTER (a-z).")
        elif guess in guessed_letters:
            print(f"  ⚠  You already guessed '{guess}'. Try another.")
        else:
            return guess


def play_hangman():
    """Main game loop."""
    print("\n" + "=" * 45)
    print("       Welcome to the Hangman Game! 🎮")
    print("=" * 45)

    word = random.choice(WORDS)
    guessed_letters = set()   
    wrong_guesses   = 0       
    max_wrong       = 6

    while wrong_guesses < max_wrong:
        display_board(wrong_guesses, guessed_letters, word)

        guess = get_player_guess(guessed_letters)
        guessed_letters.add(guess)

        if guess in word:
            print(f"  ✅ Good guess! '{guess}' is in the word.")

            if all(letter in guessed_letters for letter in word):
                display_board(wrong_guesses, guessed_letters, word)
                print("=" * 45)
                print(f"  🎉 You WON! The word was: '{word}'")
                print("=" * 45 + "\n")
                break
        else:
            wrong_guesses += 1
            print(f"  ❌ Wrong! '{guess}' is NOT in the word.")

    else:

        display_board(wrong_guesses, guessed_letters, word)
        print("=" * 45)
        print(f"  💀 Game Over! The word was: '{word}'")
        print("=" * 45 + "\n")


def main():
    """Entry point — allows the player to play multiple rounds."""
    while True:
        play_hangman()
        again = input("  Play again? (yes / no): ").lower().strip()
        if again not in ("yes", "y"):
            print("\n  Thanks for playing! Goodbye 👋\n")
            break


if __name__ == "__main__":
    main()