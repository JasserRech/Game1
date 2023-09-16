import game
from clear import clear

def initial_screen():
    while True:
        play_game = str(input('Do you want to play a game? (y/n): ')) 
        if play_game in 'yYnN':
            return play_game



while True:
    play = initial_screen()
    if play in 'Yy':
        while True:
            clear()
            game.run()
            play_again = str(input('Do you want to play again? (y/n): '))
            if play_again == 'n':
                break
            clear()
    if play in 'Nn':
        break
    clear()