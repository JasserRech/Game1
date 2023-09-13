import random
from time import sleep

suits_values = {
    'J': 10,
    'Q': 10,
    'K': 10,
    'A': 11,
}

# Criar deck
def new_deck():
    suits = ['\u2663', '\u2666', '\u2665', '\u2660']
    ranks = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
    deck = []
    for suit in suits:
        for value in ranks:
            deck.append(f'{value} {suit}')
    random.shuffle(deck)
    return deck