from typing import List


def filter_words(word_len: int, output_file: str):
    words: List = []
    with open('5000-words.txt') as f:
        words = f.readlines()

    output = []
    for word in words:
        if len(word) == word_len + 1:
            output += word

    with open(output_file, 'w') as f:
        f.writelines(output)


filter_words(5, "5-char-words.txt")
filter_words(6, "6-char-words.txt")
filter_words(7, "7-char-words.txt")
