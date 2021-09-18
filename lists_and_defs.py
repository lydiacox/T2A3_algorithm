import random
import os

# Got list through to "yesterday" from https://onlymyenglish.com/common-noun-list/
# Thought those words were a bit boring so added more interesting ones.
dictionary = ["adult", "age", "amount", "area", "back", "bed", "blood", "body", "book", "box", "boy", "bulb", "bunch", "business", "camera", "chicken", "child", "chocolates", "city", "clothes", "colony", "colours", "company", "computer", "continent", "council", "country", "course", "cycle", "dates", "day", "death", "desk", "door", "egg", "face", "fact", "factory", "family", "farm", "farmer", "father", "fish", "floor", "flowers", "flood", "fridge", "food", "future", "game", "garden", "gas", "glass", "group", "health", "hill", "hospital", "idea", "image", "industry", "island", "jewellery", "job", "kitchen", "land", "law", "leaves", "leg", "letter", "life", "magazine", "market", "metal", "mirror", 'mobile', 'money', 'morning', 'mother', 'mountain', 'movie', 'name', 'nest', 'news', 'ocean', 'oil', 'painter', 'park', 'party', 'pen', 'pencil', 'person', 'picture', 'pillow', 'place', 'plant', 'pond', 'rain', 'rate', 'result', 'ring', 'road', 'rock', 'rocket', 'room', 'rope', 'rule', 'sale', 'school', 'shape', 'ship', 'shop', 'sister', 'site', 'skin',
              'snacks', 'son', 'song', 'sort', 'sound', 'soup', 'sports', 'state', 'stone', 'street', 'system', 'taxi', 'tea', 'teacher', 'team', 'toy', 'tractor', 'trade', 'train', 'video', 'view', 'water', 'waterfall', 'week', 'women', 'wood', 'word', 'year', 'yesterday', 'bumfuzzle', 'lollygag', 'collywobbles', 'lackadaisical', 'woebegone', 'bloviate', 'malarky', 'hullaballoo', 'dongle', 'bodacious', 'flibbertigibbet', 'bamboozle', 'kerfuffle', 'discombobulate', 'brouhaha', 'cattywampus', 'billingsgate', 'comeuppance', 'nincompoop', 'cantankerous', 'cockamamie', 'codswallop', 'mollycoddle', 'pettifogger', 'rigmarole', 'shenanigan', 'skedaddle', 'bumbershoot', 'lickspittle', 'sozzled', 'canoodle', 'foolscap', 'flummery', 'sobersides', 'skirl', 'wamble', 'stumblebum', 'grommet', 'blunderbuss', 'ragamuffin', 'confabulate', 'dragooned', 'mercurial', 'frippery', 'lothario', 'waggish', 'taradiddle', 'widdershins', 'sialoquent', 'wabbit', 'impignorate', 'quagmire', 'ratoon', 'xertz', 'fartlek', 'obelus', 'titter', 'whippersnapper', 'flabbergast', 'tubular']

# Find out if there are one or two players, error handling for any entry other than "1" or "2"


def get_players():
    players = False
    while players == False:
        players = input('Are there 1 or 2 players?: ')
        if (players != '1') and (players != '2'):
            print('Please enter "1" or "2"')
            players = False
    return players

# Clear the screen so Player 2 doesn't see the word they're meant to be guessing


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# Get the word to guess, either from the dictionary above or as entered by Player 1. Error handling for input other than a thru z.


def get_word(players):
    word = False
    while word == False:
        if players == '1':
            word = random.choice(dictionary)
        elif players == '2':
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
