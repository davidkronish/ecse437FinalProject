""" 
A file for all game functions
"""


def input_chips():
    while True: 
        try:
            chip_amt = int(input("Enter the amount in chips you'd like to purchase: "))
        except:
            print("Invalid Entry. Please provide an integer as the numher of chips you'd like to buy.")
        else:
            break 
    return chip_amt



def take_bet(chips):
    while True: 
        try: 
            chips.bet = int(input("How many chips would you like to bet? \t"))
        except: 
            print("Invalid Entry. Please provide an integer as a bet.")
        else: 
            if chips.bet > chips.total:
                print(f'You currenlty do not have enough chips to make this bet. Your current chip total is {chips.total}')
            else: 
                break


def double_option(chips):
    double_op = input("Would you like to double the bet? y/n: ")
    if double_op[0].lower() == 'y':
        if chips.total < chips.bet*2:
            print(f"You don't have enough chips to double the bet. Bet stands as is at {chips.bet}")
        else: 
            chips.bet = chips.bet*2
            print(f"The current bet is now: {chips.bet}")


def hit(deck,hand):
    single_card = deck.deal()
    hand.add_card(single_card)
    hand.adjust_for_aces()

def show_some(player, dealer):
    #Show only ONE of the dealer's cards 
    print(f"The dealer's hand: [ 'Hidden Card', '{dealer.cards[1]}']")
    #show all cards of the player's hand/cards. 
    print(f"The player's hand: {player.get_hand_cards()} has value {player.value}")


def show_all(player, dealer):
    #Show all of the dealer's cards 
    print(f"The dealer's hand: {dealer.get_hand_cards()} has value {dealer.value}")
    #show all cards of the player's hand/cards. 
    print(f"The player's hand: {player.get_hand_cards()} has value {player.value}")


#end of game scenarios
def player_wins_off_blackjack(player, dealer,chips):
    print("Blackjack! Player wins 1.5x bet.")
    chips.win_blackjack()


def player_busts(player, dealer, chips):
    print("Player Busts!")
    chips.lose_bet()

def player_wins(player, dealer, chips):
    print("Player Wins!")
    chips.win_bet()

def dealer_busts(player, dealer, chips):
    print("Dealer Busts!")
    chips.win_bet()


def dealer_wins(player, dealer, chips):
    print("Dealer Wins!")
    chips.lose_bet()


def push(player, dealer):
    print("Dealer and player tie! PUSH!")
