import random

def hangman():
   
    words = ["apple", "banana", "orange", "grape", "mango"]
    word = random.choice(words)
    guessed = ["_"] * len(word)  
    attempts = 6  
    guessed_letters = []  

    print("🎮 Welcome to Hangman!")
    print("Guess the word: " + " ".join(guessed))

    while attempts > 0 and "_" in guessed:
        guess = input("Enter a letter: ").lower()

        if not guess.isalpha() or len(guess) != 1:
            print("❌ Please enter a single alphabet letter.")
            continue

        if guess in guessed_letters:
            print("⚠️ You already guessed that letter.")
            continue

        guessed_letters.append(guess)

        if guess in word:
            print("✅ Correct guess!")
            for i, letter in enumerate(word):
                if letter == guess:
                    guessed[i] = guess
        else:
            attempts -= 1
            print(f"❌ Wrong guess! Attempts left: {attempts}")

        print(" ".join(guessed))

    # Game result
    if "_" not in guessed:
        print("🎉 Congratulations! You guessed the word:", word)
    else:
        print("💀 Game Over! The word was:", word)

# Run the game
hangman()
