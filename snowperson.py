import lists_and_defs
import ascii_art


def play_game():
    won_lost = False
    melts = 0
    letters_guessed = []
    lists_and_defs.clear_screen()
    print(ascii_art.game_name)
    print('Welcome to Snowman! Guess the word or your Snowman will melt!')
    while won_lost == False:
        players = lists_and_defs.get_players()
        word = lists_and_defs.get_word(players)
        hidden = lists_and_defs.hide(word)
        lists_and_defs.clear_screen()
        message = 'Let\'s play Snowman!'
        while melts < 7:
            print(ascii_art.snow_scenes[melts])
            print(message)
            print(hidden)
            guess = lists_and_defs.valid_guess()
            # I would have liked this block of code to be in lists_and_defs.py, but as the functions change variables or append to lists within this file, I could not. I would have had to import snowperson.py into lists_and_defs.py, which would have created an infinite loop.
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
                    hidden = lists_and_defs.currently_revealed(
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
    again = lists_and_defs.play_again()
    if again == 'Y':
        play_game()
    else:
        exit()


play_game()
