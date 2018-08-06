def hangman(word):
    """
    guess the word before printing out hanging man

    param rletters: the list of the word
    param guess: a list of _
    param man: a list of special characters
    param wrong: int to count number of wrong guesses
    param right: int to count the number of correct guesses
    param a: string to hold the guess
    param cind: int to locate the charac
    
    """
    rletters = list(word)
    guess = list("_"*len(word))
    man = ["|    ___    |",
           "|   _   _   |",
           "|  _     _  |",
           "|   _   _   |",
           "|    |  |   |",
           "| ---    ---|",
           "| ___    ___|",
           "|    |  |   |",
           "|    |  |   |",
           "|   /    \  |",
           "|  /      \ |"]

    wrong = 0
    right = 0
    while wrong < len(man) -1 :
        a = input("Please guess a character of the word: ")
        if a in word:
            cind = rletters.index(a)
            guess[cind] = a
            rletters[cind] = "$"
            print(guess)
            right += 1
        else:
            wrong += 1
            print("\n".join(man[0:wrong]))
        if right == len(word):
            print("Win")
            break


import random 
word_list = ["cat", "wood", "face", "computer", "tv",
             "seattle"]
num = random.randint(0, len(word_list)+1)
hangman(word_list[num])

