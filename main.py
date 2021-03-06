import letterFunctions
import hangmanPatterns
from string import ascii_letters
from random import choice


def list_to_string(list_of_strings, separator=""):
    if separator == "":
        string = "".join(list_of_strings)
    else:
        string = ""
        for item in list_of_strings:
            if item == list_of_strings[-1]:
                string += item
            else:
                string += item + separator
    return string


f = open("words.txt")
list_with_words = []
for line in f:
    line.replace("\n", "")
    list_with_words.append(line)
f.close()

line = "=============================================="

word = choice(list_with_words).strip()
guess = ...
guessed_word = ""
typedLetters = []

for letter in word:
    if letter not in ascii_letters:
        print(f"Error in symbol from word \"{word}\" from word list!")
    guessed_word += "_"

mistakes = 0

while guessed_word != word and mistakes < 10:
    guess = input("Type letter: ").lower()

    if len(guess) != 1:
        print("Letter can be only 1 character")
        continue

    if guess not in ascii_letters:
        print("This isn't letter")
        continue

    if guess in typedLetters:
        print("You typed this letter before")
        continue

    typedLetters.append(guess)
    typedLetters.sort()

    correct_guess = letterFunctions.is_in_word(guess, word)

    if correct_guess:
        indexes_to_replace = letterFunctions.get_indexes_in_word(guess, word)

        guessed_word = list(guessed_word)
        for i in range(len(indexes_to_replace)):
            guessed_word[indexes_to_replace[i]] = guess
        guessed_word = list_to_string(guessed_word)

        indexes_to_replace = []
        print(hangmanPatterns.draw_hangman(mistakes))
        print(guessed_word)
        print(f"Typed letters: {list_to_string(typedLetters, ', ')}")
        print(f"\n{line}\n")

    else:
        mistakes += 1

        print(hangmanPatterns.draw_hangman(mistakes))
        print(guessed_word)
        print(f'Typed letters: {list_to_string(typedLetters, ", ")}')
        print(f'\n{line}\n')

        continue

if word == guessed_word:
    print(f"Congratulations you win!")
else:
    print(f"You lost! The word is {word}")
