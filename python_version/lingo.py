from typing import List
from random import choice


class Board:
    def __init__(self, word_len: int) -> None:
        self.board: List[str] = [['' for _ in range(word_len)] for _ in range(5)]

    def set_word(self, row: int, word) -> None:
        word = [letter for letter in word]
        self.board[row] = word

    def display(self) -> None:
        for row in self.board:
            print(row)


class Word:
    def __init__(self, word_len: int) -> None:
        words: List[str] = self.__parse_words(word_len)
        self.secret_word: str = choice(words).strip()
        self.guessed_so_far: List[str] = ['' for _ in range(word_len)]

    def __parse_words(self, word_len: int) -> List[str]:
        if word_len == 5:
            with open('C:\\Users\\tjalw\\Documents\\GitHub\\lingo.vue\\python_version\\resources\\5-char-words.txt') as file:
                words = file.readlines()
        elif word_len == 6:
            with open('C:\\Users\\tjalw\\Documents\\GitHub\\lingo.vue\\python_version\\resources\\6-char-words.txt') as file:
                words = file.readlines()
        else:
            with open('C:\\Users\\tjalw\\Documents\\GitHub\\lingo.vue\\python_version\\resources\\5-char-words.txt') as file:
                words = file.readlines()

        stripped_words = []
        for word in words:
            stripped_words.append(word.strip())

        return stripped_words

    def guess(self, guess:
              str) -> None:
        semi_guess = []
        for i, letter in enumerate(guess):
            if letter == self.secret_word[i]:
                semi_guess[i] = letter
            else:
                semi_guess[i] = ''

        for i, letter in enumerate(semi_guess):
            if self.guessed_so_far[i] == '':
                self.guessed_so_far[i] == letter

    def is_guessed(self):
        return self.guessed_so_far == self.secret_word


class Player:
    def __init__(self, name) -> None:
        self.name = name
