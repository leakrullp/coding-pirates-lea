import random

def hangman():
    words = ["python", "computer", "hangman", "programming", "university"]
    word = random.choice(words).lower()
    guessed = ["_"] * len(word)
    used_letters = set()
    attempts = 6  # number of wrong guesses allowed

    print("🎮 Welcome to Hangman!")
    print("The word has", len(word), "letters.")
    print(" ".join(guessed))

    while attempts > 0 and "_" in guessed:
        guess = input("Guess a letter: ").lower()

        if not guess.isalpha() or len(guess) != 1:
            print("Please enter a single letter.")
            continue

        if guess in used_letters:
            print("You already guessed that letter. Try again.")
            continue

        used_letters.add(guess)

        if guess in word:
            print("✅ Correct!")
            for i, letter in enumerate(word):
                if letter == guess:
                    guessed[i] = guess
        else:
            attempts -= 1
            print("❌ Wrong guess. Attempts left:", attempts)

        print("Word:", " ".join(guessed))
        print("Used letters:", " ".join(sorted(used_letters)))

    if "_" not in guessed:
        print("🎉 You won! The word was:", word)
    else:
        print("💀 Game over! The word was:", word)

# Run the game
hangman()
