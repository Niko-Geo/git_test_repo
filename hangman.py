from getpass import getpass

def get_secret_word():
    """
    Ask the user for the secret word and ensure:
    - it is not empty
    - it contains only letters (a-z)
    """
    while True:
        word = getpass("Enter the secret word (player 1): ").strip().lower()

        if len(word) == 0:
            print("The word cannot be empty. Please try again.")
            continue

        if not word.isalpha():
            print("The word must contain letters only (a-z). Please try again.")
            continue

        return word



def create_initial_state(secret_word):
    """
    Initialize and return the game state.
    """
    guessed_letters = []
    wrong_guesses = 0
    max_attempts = 6  # you can change this if you like
    return guessed_letters, wrong_guesses, max_attempts


def print_game_state(secret_word, guessed_letters, wrong_guesses, max_attempts):
    """
    Print the current state of the game:
    - the word with underscores for unknown letters
    - number of wrong guesses
    - letters already guessed
    """
    display_letters = []
    for ch in secret_word:
        if ch in guessed_letters:
            display_letters.append(ch)
        else:
            display_letters.append("_")

    # Join with spaces so it looks like: b a _ a _ a
    display_word = " ".join(display_letters)

    print("\nCurrent word:")
    print(display_word)
    print(f"Wrong guesses: {wrong_guesses}/{max_attempts}")

    if guessed_letters:
        print("Guessed letters:", ", ".join(guessed_letters))
    else:
        print("Guessed letters: (none yet)")


def get_player_guess(guessed_letters):
    """
    Ask the player to guess a single new letter.
    Keep asking until the input is valid.
    """
    while True:
        guess = input("\nGuess a letter: ").strip().lower()

        if len(guess) != 1:
            print("Please enter exactly one character.")
            continue

        if not guess.isalpha():
            print("Please enter a letter (a-z).")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter. Try another one.")
            continue

        return guess


def update_state(secret_word, guessed_letters, wrong_guesses, guess):
    """
    Update the game state with the new guess.
    Return the updated guessed_letters and wrong_guesses.
    """
    guessed_letters.append(guess)

    if guess not in secret_word:
        wrong_guesses += 1
        print(f"'{guess}' is not in the word.")
    else:
        print(f"Good job! '{guess}' is in the word.")

    return guessed_letters, wrong_guesses


def check_win(secret_word, guessed_letters):
    """
    Check if all letters in secret_word have been guessed.
    Return True if player has won, otherwise False.
    """
    for ch in secret_word:
        if ch not in guessed_letters:
            return False
    return True


def main():
    print("=== Hangman ===")

    while True:
        secret_word = get_secret_word()

        # Optional: clear screen a bit so Player 2 can't see the word
        print("\n" * 50)

        guessed_letters, wrong_guesses, max_attempts = create_initial_state(secret_word)

        # Game loop
        while wrong_guesses < max_attempts:
            print_game_state(secret_word, guessed_letters, wrong_guesses, max_attempts)

            guess = get_player_guess(guessed_letters)

            guessed_letters, wrong_guesses = update_state(
                secret_word,
                guessed_letters,
                wrong_guesses,
                guess
            )

            if check_win(secret_word, guessed_letters):
                print_game_state(secret_word, guessed_letters, wrong_guesses, max_attempts)
                print("\n🎉 You won! The word was:", secret_word)
                break

        # If the loop ended due to too many wrong guesses
        if not check_win(secret_word, guessed_letters):
            print_game_state(secret_word, guessed_letters, wrong_guesses, max_attempts)
            print("\n💀 You lost! The word was:", secret_word)

        # Play again?
        while True:
            again = input("\nDo you want to play again? (y/n): ").strip().lower()
            if again in ("y", "n"):
                break
            else:
                print("Please enter 'y' or 'n'.")

        if again == "n":
            print("\nThanks for playing Hangman!")
            break



if __name__ == "__main__":
    main()
