WRONG_GUESSES = 0


def enter_word():
    word = str(input("Enter a Word that has to be guessed: "))
    letters = list(word.lower())
    return letters


def enter_letter(word, guessed_letters):
    global WRONG_GUESSES
    letter = str(input("Enter a letter you want to guess: ")).lower()
    if letter in word:
        print("The letter is in the word!")
        # Update guessed_letters to reveal correct guesses
        for i in range(len(word)):
            if word[i] == letter:
                guessed_letters[i] = letter
    else:
        print("The letter is not in the word!")
        WRONG_GUESSES += 1


def show_status(n_wrong_guesses):
    graphics = ['''
      +---+
      |   |
          |
          |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
          |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
      |   |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
     /|   |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
     /|\  |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
     /|\  |
     /    |
          |
    =========''', '''
      +---+
      |   |
      O   |
     /|\  |
     / \  |
          |
    =========''']
    if n_wrong_guesses == 0:
        return "No wrong guesses!"
    else:
        return graphics[n_wrong_guesses - 1]


def play():
    global WRONG_GUESSES
    word = enter_word()
    guessed_letters = ["_"] * len(word)  # Initialize guessed_letters with underscores

    while WRONG_GUESSES < 7 and "_" in guessed_letters:
        enter_letter(word, guessed_letters)
        print("Current word status: ", " ".join(guessed_letters))
        print(show_status(WRONG_GUESSES))

    if "_" not in guessed_letters:
        print("Congratulations! You've guessed the word:", "".join(guessed_letters))
    else:
        print("Too many mistakes, you lost! The word was:", "".join(word))


if __name__ == "__main__":
    play()
