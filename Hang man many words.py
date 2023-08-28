import random


def hangman():
    words = ["python", "programming", "computer", "keyboard", "developer", "algorithm", "variable" , "sherlock"]
    word = random.choice(words)
    guessed_letters = []
    tries = 4

    while tries > 0:
        guessed_word = ""
        for letter in word:
            if letter in guessed_letters:
                guessed_word += letter
            else:
                guessed_word += "_"

        if guessed_word == word:
            print("\t\t\t You Win ^_^ !!")
            break

        print(guessed_word)

        guess = input("\n Enter letter : ")

        if len(guess) != 1:
            print(" \n Just enter one letter")
            continue

        if guess in guessed_letters:
            print("\n You entered this letter before.")
        elif guess in word:
            guessed_letters.append(guess)
            print("\n true!")
        else:
            tries -= 1
            print(f" \n Wrong still {tries} tries.")

    if tries == 0:
        print(f" \n\n I am sorry You loss the word was : {word}")


hangman()

