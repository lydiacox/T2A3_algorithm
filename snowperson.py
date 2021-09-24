import ascii_art
import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def get_word():
    word = False
    while word == False:
        word = input(
            'What word would you like Player 2 to guess? (A thru Z only.) Make sure they can\'t see your screen!:\n')
        if not word.isalpha():
            print('Please only use letters (a thru z)')
            word = False
        elif len(word) < 2:
            print('At least two characters, please.')
            word = False
    return word.upper()

# Hide all the letters in the word


def hide(word):
    hidden = '_' * len(word)
    return hidden

# Get the guess, error handling for input other than a thru z.

def valid_guess():
    valid_guess = False
    while valid_guess == False:
        valid_guess = input('Guess a letter or word: ')
        if not valid_guess.isalpha():
            print('Only letters (a thru z)')
            valid_guess = False
    return valid_guess.upper().strip()

# Using the most recent guess, the full word to be guessed and the current state of the hidden word, reveal letters at the index where that letter in the word matches the guess.


def currently_revealed(guess, word, hidden):
    hidden = list(hidden)
    for index, letter in enumerate(word):
        if guess == letter:
            hidden[index] = guess
    return ''.join(hidden)

# Ask player(s) if they want to play again, error handling for input other than "Y" or "N".


def play_again():
    again = False
    while again == False:
        again = input('Do you want to play again? (Y/N): ').upper()
        if again == 'Y' or again == 'N':
            return again
        else:
            print('Please use Y or N')
            again = False

def play_game():
    won_lost = False
    melts = 0
    letters_guessed = []
    clear_screen()
    print(ascii_art.game_name)
    print('Welcome to Snowman! Guess the word or your Snowman will melt!')
    while won_lost == False:
        word = get_word()
        hidden = hide(word)
        clear_screen()
        message = 'Let\'s play Snowman!'
        while melts < 7:
            print(ascii_art.snow_scenes[melts])
            print(message)
            print(hidden)
            guess = valid_guess()
            if len(guess) == 1:
                if guess in letters_guessed:
                    message = 'Choose another letter, you already guessed that one.'
                elif not guess in word:
                    message = 'Nope, try again!'
                    melts += 1
                    letters_guessed.append(guess)
                else:
                    message = 'Yep, you got one!'
                    letters_guessed.append(guess)
                    hidden = currently_revealed(
                        guess, word, hidden)
                    if hidden == word:
                        won_lost = 'Won'
                        melts = 9
            elif len(guess) == len(word):
                if guess == word:
                    won_lost = 'Won'
                    melts = 9
                else:
                    message = 'Nope, that\'s not it!'
                    melts += 1
            else:
                print('Please enter a single letter or guess the whole word.')
        if melts == 7:
            won_lost = 'Lost'
    if won_lost == 'Won':
        print(ascii_art.snowflakes)
        print(f'YOU GOT IT! {word} was the word!')
    else:
        print(ascii_art.snow_scenes[7])
        print(
            f'Your snowman melted! :-( The word was {word}. Better luck next time!')
    again = play_again()
    if again == 'Y':
        play_game()
    else:
        exit()


play_game()