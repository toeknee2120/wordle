import random
from colors import bcolors

print(f'{bcolors.GREEN}HELLO{bcolors.END}')

wordlist = (
    'apple',
    'mango',
    'month',
    'crave',
    'moths',
)



def pick_word():
    return random.choice(wordlist)

def play_game():
    word = pick_word()
    print(word)

    guesses = 5

    while guesses > 0:
        
        guess = input("Enter a 5 character word: ").casefold()

        for index, character in enumerate(word):
            if word[index] == guess[index]:
                print('{bcolors.GREEN}HELLO{bcolors.END}')

        guesses -= 1



if __name__ == "__main__":
    play_game()
    






