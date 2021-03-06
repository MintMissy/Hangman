import letterFunctions
import hangmanPatterns
from string import ascii_letters


def list_to_string(list):
    string = "".join(list)
    return string


line = "=============================================="

word = "example"
guess = ...
guessed_word = ""

for letter in word:
    if letter not in ascii_letters:
        print(f"Error in word \"{word}\" from word list!")
        pass
    guessed_word += "_"

mistakes = 0

while guessed_word != word and mistakes < 10:
    guess = input("Type letter\n").lower()

    if len(guess) != 1:
        print("Letter can be a symbol from [a-z] or [A-Z]")
        pass

    correct_guess = letterFunctions.is_in_word(guess, word)

    if correct_guess:
        indexes_to_replace = letterFunctions.get_indexes_in_word(guess, word)

        guessed_word = list(guessed_word)
        for i in range(len(indexes_to_replace)):
            guessed_word[indexes_to_replace[i]] = guess
        guessed_word = list_to_string(guessed_word)

        indexes_to_replace = []

        print(f"Nice guess\n"
              f"\n"
              f"{hangmanPatterns.draw_hangman(mistakes)}")
        print(guessed_word)
        print("\n")
        print(line)

    else:
        mistakes += 1

        print(f"I don't see this letter in word\n"
              f"\n"
              f"{hangmanPatterns.draw_hangman(mistakes)}")
        print(guessed_word)
        print("\n")
        print(line)
        pass

if word == guessed_word:
    print(f"{line}\n"
          f"Congratulations you win!\n"
          f"{line}")
else:
    print(f"\n"
          f"{line}\n"
          f"You lost :c! Word: {word}\n"
          f"{line}")
