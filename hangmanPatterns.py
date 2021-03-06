def draw_hangman(mistake):
    pattern_dictionary = {
        0: pattern_0,
        1: pattern_1,
        2: pattern_2,
        3: pattern_3,
        4: pattern_4,
        5: pattern_5,
        6: pattern_6,
        7: pattern_7,
        8: pattern_8,
        9: pattern_9,
        10: pattern_10,
    }
    return pattern_dictionary[mistake]


pattern_0 = (
    f"                    \n"
    f"                    \n"
    f"                    \n"
    f"                    \n"
    f"                    \n"
    f"                    \n"
)

pattern_1 = (
    f"                    \n"
    f"                    \n"
    f"                    \n"
    f"                    \n"
    f"                    \n"
    f"____________________\n"
)

pattern_2 = (
    f"|                   \n"
    f"|                   \n"
    f"|                   \n"
    f"|                   \n"
    f"|                   \n"
    f"|___________________\n"
)

pattern_3 = (
    f"-----------         \n"
    f"|                   \n"
    f"|                   \n"
    f"|                   \n"
    f"|                   \n"
    f"|___________________\n"
)

pattern_4 = (
    f"---/-------         \n"
    f"| /                 \n"
    f"|/                  \n"
    f"|                   \n"
    f"|                   \n"
    f"|___________________\n"
)

pattern_5 = (
    f"---/----|--         \n"
    f"| /     O           \n"
    f"|/                  \n"
    f"|                   \n"
    f"|                   \n"
    f"|___________________\n"
)

pattern_6 = (
    f"---/----|--         \n"
    f"| /     O           \n"
    f"|/      |           \n"
    f"|                   \n"
    f"|                   \n"
    f"|___________________\n"
)

pattern_7 = (
    f"---/----|--         \n"
    f"| /     O           \n"
    f"|/     /|           \n"
    f"|                   \n"
    f"|                   \n"
    f"|___________________\n"
)

pattern_8 = (
    f"---/----|--         \n"
    f"| /     O           \n"
    f"|/     /|\          \n"
    f"|                   \n"
    f"|                   \n"
    f"|___________________\n"
)

pattern_9 = (
    f"---/----|--         \n"
    f"| /     O           \n"
    f"|/     /|\          \n"
    f"|      /            \n"
    f"|                   \n"
    f"|___________________\n"
)

pattern_10 = (
    f"---/----|--         \n"
    f"| /     O           \n"
    f"|/     /|\          \n"
    f"|      / \          \n"
    f"|                   \n"
    f"|___________________\n"
)
