import random
import os
guesses = []
Xguesses = 0

def hangman_drawn(wrong_guesses):
    if wrong_guesses == 5:
        print("You loose!")
        return True
    else:
        return False
    #end if
#end func

def draw_hangman(wrong_guesses):
    if wrong_guesses == 1:
        print("|/      |")
    elif wrong_guesses == 2:
        print("|/      |")
        print("|      (_)")
    elif wrong_guesses == 3:
        print("|/      |")
        print("|      (_)")
        print("|      \\|/")
    elif wrong_guesses == 4:
        print("|/      |")
        print("|      (_)")
        print("|      \\|/")
        print("|       |")
    elif wrong_guesses == 5:
        print("|/      |")
        print("|      (_)")
        print("|      \\|/")
        print("|       |")
        print("|      / \\")
    else:
        print("")
    #endif
#end func

def display_word(word, guesses):
    missing_letters = len(word)
    for i in word:
        if i in guesses:
            print(i, end=" ")
            missing_letters = missing_letters - 1
        else:
            print("_", end=" ")
        #end if
    #next
    return missing_letters
#end func

path = 'C:/Users/Joshua/Documents/Words.txt'
Words_file = open(path,'r')
words = []

for i in range(0,10):
    w = Words_file.readline()
    w = w[0:(len(w)-1)]
    words.append(w)
Words_file.close()

ran_word = random.choice(words)
print("Time to play hangman")
game_over = False
while game_over == False:
##    os.system('cls')
    remaining = display_word(ran_word, guesses)
    guess = input("Guess a letter: ")
    if guess not in ran_word:
        Xguesses = Xguesses + 1
    #endif
    guesses.append(guess)
    draw_hangman(Xguesses)
    game_over = hangman_drawn(Xguesses)
    print("Guesses so far:", *guesses,)
    if remaining == 0:
        game_over = True
        print("You win!")
    #endif
#end while
