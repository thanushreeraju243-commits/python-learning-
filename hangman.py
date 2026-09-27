import random
words = ["python", "hangman", "programming", "computer", "algorithm"]
hangman_stages = {"0":"",
                  "1":"o",
                  "2":"o\n |",
                  "3":"o\n/|",
                  "4":"o\n/|\\",
                  "5":"o\n/|\\\n/",
                  "6":"o\n/|\\\n/ \\"}
def display_hangman(wrong_guesses):
    for line in hangman_stages[str(wrong_guesses)].split("\n"):
        print(line)
def display_hint(hint):
    print("Hint: " + " ".join(hint))
def main():
    while True:
        word = random.choice(words)
        hint = ["_"] * len(word)
        wrong_guesses = 0
        guessed_letters = []
        while wrong_guesses < 6 and "_" in hint:
            display_hangman(wrong_guesses)
            display_hint(hint)
            guess = input("Guess a letter: ").lower()
            if guess in guessed_letters:
                print("You already guessed that letter.")
                continue
            guessed_letters.append(guess)
            if guess in word:
                for i, letter in enumerate(word):
                    if letter == guess:
                        hint[i] = guess
            else:
                wrong_guesses += 1
        if "_" not in hint:
            print("Congratulations! You guessed the word: " + word)
        else:
            display_hangman(wrong_guesses)
            print("Game over! The word was: " + word)
        play_again = input("Do you want to play again? (y/n): ").lower()
        if play_again != "y":
            break
if __name__ == "__main__":
    main()
    
