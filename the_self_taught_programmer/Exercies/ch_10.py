# The Hangman
def hangman(word):
    wrong = 0
    stages = ["                  ",
              "|__________       ",
              "|         |       ",
              "|         |       ",
              "|         0       ",
              "|        /|\      ",
              "|        / \      ",
              "|                 "
              ]
    rletters = list(word)
    # Why list ["_"]?
    board = ["_"] * len(word)
    win = False
    print('Welcome')
    while wrong < len(stages) - 1:
        print("\n")
        msg = 'Type letter: '
        char = input(msg)
        if char in rletters:
            cind = rletters.index(char)
            board[cind] = char
            rletters[cind] = '$'
        else:
            wrong += 1
        print(''.join(board))
        e = wrong + 1
        print('\n'.join(stages[ :e]))
        if "_" not in board:
            print('You win! Take a cake! Right word: ')
            print(''.join(board))
            win = True
            break
    if not win:
        print('\n'.join(stages[0:wrong]))
        print('You lost! We dont have a cake for you! Right word {}'.format(word))
hangman('test')