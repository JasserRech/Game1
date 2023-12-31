import random
from time import sleep
from clear import clear


suits_values = {
    'J': 10,
    'Q': 10,
    'K': 10,
    'A': 11,
}

# function to create and shuffle deck
def new_deck():
    suits = ['\u2663', '\u2666', '\u2665', '\u2660']
    ranks = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
    deck = []
    for suit in suits:
        for value in ranks:
            deck.append(f'{value} {suit}')
    random.shuffle(deck)
    return deck


# function to print player and dealer hand
def show_result(player_hand, dealer_hand):
    clear()
    print('Player hand:')
    print(player_hand)
    print('Dealer hand:')
    print(dealer_hand)


# function to calculate cards values in hand 
def hand_sum(hand):
    value = 0
    for card in hand:
        value_temp = card.split(' ')[0]
        if value_temp in suits_values:
            value += suits_values[value_temp]
        else:
            value += int(value_temp)
    return value


# function with player moves
def playerturn(deck, player_hand, dealer_hand):
    while True:
        show_result(player_hand, dealer_hand)
        hit_or_stand = str(input('Hit or Stand? (h/s):')).lower()
        
        if hit_or_stand == 'h':
            player_hand.append(deck.pop())
            show_result(player_hand, dealer_hand)
            if hand_sum(player_hand) > 21:
                print("Player busts. Dealer wins!")
                return
            
        elif hit_or_stand == 's':
            show_result(player_hand, dealer_hand)
            return


#function with dealer moves
def dealerturn(deck, dealer_hand, player_hand):
    if 'x' in dealer_hand:
        sleep(1)
        dealer_hand.remove('x')
        dealer_hand.append(deck.pop())
        dealer_result = hand_sum(dealer_hand)
        show_result(player_hand, dealer_hand)

    while dealer_result < 17:
        sleep(1)
        dealer_hand.append(deck.pop())
        dealer_result = hand_sum(dealer_hand)
        show_result(player_hand, dealer_hand)
        
    if 17 <= dealer_result <= 21:      
        show_result(player_hand, dealer_hand)
        return
    
    elif dealer_result > 21:   
        show_result(player_hand, dealer_hand)
        print('Dealer busts. Player wins!')
        return
    
    
    


# function with main game loop
def run():
    clear()
    deck = new_deck()
    player_hand = [deck.pop(), deck.pop()]
    dealer_hand = [deck.pop(), 'x']

    playerturn(deck, player_hand, dealer_hand)
    
    if hand_sum(player_hand) > 21:
        dealer_hand.remove('x')
    if hand_sum(player_hand) <= 21:
        dealerturn(deck, dealer_hand, player_hand)
    if hand_sum(dealer_hand) == hand_sum(player_hand):
        print("It's a tie!")
    if hand_sum(dealer_hand) <= 21 and hand_sum(dealer_hand) > hand_sum(player_hand):
        print('Dealer wins!')
    if hand_sum(player_hand) <= 21 and  hand_sum(player_hand) > hand_sum(dealer_hand):
        print('Player wins!')
    