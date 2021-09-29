import ascii_art
import os
import random

# Got list through to "yesterday" from https://onlymyenglish.com/common-noun-list/
# Thought those words were a bit boring so added more interesting ones.

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def quit_game():
    print("\nThanks for playing!")
    exit()


class Word():
    '''A class to represent a word randomly selected from a list of words.

    Attributes
    ----------
    word_list : list
        A list of words.
    word : str
        The randomly selected word.
    hidden : str
        The word with underscores representing the letters to be guessed.
    '''
    word_list = ['ADULT', 'AGE', 'AMOUNT', 'AREA', 'BACK', 'BED', 'BLOOD', 'BODY', 'BOOK', 'BOX', 'BOY', 'BULB', 'BUNCH', 'BUSINESS', 'CAMERA', 'CHICKEN', 'CHILD', 'CHOCOLATES', 'CITY', 'CLOTHES', 'COLONY', 'COLOURS', 'COMPANY', 'COMPUTER', 'CONTINENT', 'COUNCIL', 'COUNTRY', 'COURSE', 'CYCLE', 'DATES', 'DAY', 'DEATH', 'DESK', 'DOOR', 'EGG', 'FACE', 'FACT', 'FACTORY', 'FAMILY', 'FARM', 'FARMER', 'FATHER', 'FISH', 'FLOOR', 'FLOWERS', 'FLOOD', 'FRIDGE', 'FOOD', 'FUTURE', 'GAME', 'GARDEN', 'GAS', 'GLASS', 'GROUP', 'HEALTH', 'HILL', 'HOSPITAL', 'IDEA', 'IMAGE', 'INDUSTRY', 'ISLAND', 'JEWELLERY', 'JOB', 'KITCHEN', 'LAND', 'LAW', 'LEAVES', 'LEG', 'LETTER', 'LIFE', 'MAGAZINE', 'MARKET', 'METAL', 'MIRROR', 'MOBILE', 'MONEY', 'MORNING', 'MOTHER', 'MOUNTAIN', 'MOVIE', 'NAME', 'NEST', 'NEWS', 'OCEAN', 'OIL', 'PAINTER', 'PARK', 'PARTY', 'PEN', 'PENCIL', 'PERSON', 'PICTURE', 'PILLOW', 'PLACE', 'PLANT', 'POND', 'RAIN', 'RATE', 'RESULT', 'RING', 'ROAD', 'ROCK', 'ROCKET', 'ROOM', 'ROPE', 'RULE', 'SALE', 'SCHOOL', 'SHAPE', 'SHIP', 'SHOP', 'SISTER', 'SITE', 'SKIN', 'SNACKS', 'SON', 'SONG', 'SORT', 'SOUND', 'SOUP', 'SPORTS', 'STATE', 'STONE', 'STREET', 'SYSTEM', 'TAXI', 'TEA', 'TEACHER', 'TEAM', 'TOY', 'TRACTOR', 'TRADE', 'TRAIN', 'VIDEO', 'VIEW', 'WATER', 'WATERFALL', 'WEEK', 'WOMEN', 'WOOD', 'WORD', 'YEAR', 'YESTERDAY', 'BUMFUZZLE', 'LOLLYGAG', 'COLLYWOBBLES', 'LACKADAISICAL', 'WOEBEGONE', 'BLOVIATE', 'MALARKY', 'HULLABALLOO', 'DONGLE', 'BODACIOUS', 'FLIBBERTIGIBBET', 'BAMBOOZLE', 'KERFUFFLE', 'DISCOMBOBULATE', 'BROUHAHA', 'CATTYWAMPUS', 'BILLINGSGATE', 'COMEUPPANCE', 'NINCOMPOOP', 'CANTANKEROUS', 'COCKAMAMIE', 'CODSWALLOP', 'MOLLYCODDLE', 'PETTIFOGGER', 'RIGMAROLE', 'SHENANIGAN', 'SKEDADDLE', 'BUMBERSHOOT', 'LICKSPITTLE', 'SOZZLED', 'CANOODLE', 'FOOLSCAP', 'FLUMMERY', 'SOBERSIDES', 'SKIRL', 'WAMBLE', 'STUMBLEBUM', 'GROMMET', 'BLUNDERBUSS', 'RAGAMUFFIN', 'CONFABULATE', 'DRAGOONED', 'MERCURIAL', 'FRIPPERY', 'LOTHARIO', 'WAGGISH', 'TARADIDDLE', 'WIDDERSHINS', 'SIALOQUENT', 'WABBIT', 'IMPIGNORATE', 'QUAGMIRE', 'RATOON', 'XERTZ', 'FARTLEK', 'OBELUS', 'TITTER', 'WHIPPERSNAPPER', 'FLABBERGAST', 'TUBULAR']

    def __init__(self):
        self.word = random.choice(self.word_list)
        self.hidden = '_' * len(self.word)


# Get the guess, error handling for input other than a thru z.
def valid_guess():
    try:
        valid_guess = False
        while valid_guess == False:
            valid_guess = input('Guess a letter or word: ')
            if not valid_guess.isalpha():
                print('Only letters (a thru z)')
                valid_guess = False
        return valid_guess.upper().strip()
    except KeyboardInterrupt:
        quit_game()


# Using the most recent guess, the full word to be guessed and the current state of the hidden word, reveal letters at the index where that letter in the word matches the guess.
def currently_revealed(guess, word, hidden):
    hidden = list(hidden)
    for index, letter in enumerate(word):
        if guess == letter:
            hidden[index] = guess
    return ''.join(hidden)



class Game():
    '''A class to represent the game!

    ...

    Attributes
    ----------

    Methods
    -------
    '''
    
    def play_again():
        try:
            again = False
            while again == False:
                again = input('Do you want to play again? (Y/N): ').upper()
                if again == 'Y' or again == 'N':
                    return again
                else:
                    print('Please use Y or N')
                    again = False
        except KeyboardInterrupt:
            quit_game()

class Snow():
    pass

def play_game():
    won_lost = False
    melts = 0
    letters_guessed = []
    clear_screen()
    print(ascii_art.game_name)
    print('Welcome to Snowman! Guess the word or your Snowman will melt!')
    try:
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
    except KeyboardInterrupt:
        quit_game()
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
        quit_game()