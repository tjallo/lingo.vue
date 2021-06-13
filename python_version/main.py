from lingo import Board, Word, Player



def main():
    word_len = 5
    board = Board(word_len)
    word = Word(word_len)
    player = Player("Tesatna")
    print(word.secret_word)

    while not word.is_guessed(): 
        board.display()
        guess = input()
        word.guess(guess.strip())



if __name__ == '__main__':
    main()