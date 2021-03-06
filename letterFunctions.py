from string import ascii_letters


def is_in_word(letter, word):
    if letter in word:
        return True
    else:
        return False


def is_enabled(letter):
    if letter in ascii_letters:
        return True
    else:
        return False


def get_indexes_in_word(letter, word):
    indexes = []
    for i in range(len(word)):
        if word[i] == letter:
            indexes.append(i)
    return indexes
