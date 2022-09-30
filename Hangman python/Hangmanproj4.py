import random
from words import wors
import string
def get_valid_words(wors):
    word=random.choice(wors)
    while "-" in word or " " in word:
        word = random.choice(wors)
    return word.upper()
def hangman():
    cho_word = get_valid_words(wors)
    alphabet= set(string.ascii_uppercase)
    words=set(cho_word)
    used_letter=set()
    lives=10
    while(len(words)>0 and lives>0):
        print("The letters you have used is",' '.join(used_letter))
        user_input = input("Enter a cHaracter: ").upper()

        if( user_input in alphabet - used_letter ):
            used_letter.add(user_input)
            if(user_input in words):
                words.remove(user_input)
            else:
                print("wrong,lost one lives")
                lives=lives-1
        elif user_input in used_letter:
            print("you have already enterd ")
        else:
            print("Please enter valid character")
        print([letter if letter in used_letter else "_" for letter in cho_word])
    if(lives==0):
        print("oops! you lost the word is",cho_word)
    else:
        print("you win ",cho_word)
hangman()
