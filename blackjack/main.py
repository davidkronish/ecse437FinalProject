import sys, os
from . import Deck, Hand, Player
from gamefunctions import input_chips, take_bet, double_option, hit, show_some, show_all, player_wins_off_blackjack, player_busts, player_wins, dealer_busts, dealer_wins, push

def main():
    print("WELCOME TO BLACKJACK ! ")
    name = str(input("Enter your player name: "))
    chip_amt = input_chips()

    p = Player(name,chip_amt)

    while True:

        #Set up the game, and shuffle the deck evenly
        deck = Deck()
        deck.shuffle()

        #set up player hand
        player_hand = Hand()
        player_hand.add_card(deck.deal())
        player_hand.add_card(deck.deal())
        player_hand.adjust_for_aces()

        #set up dealer hand
        dealer_hand = Hand()
        dealer_hand.add_card(deck.deal())
        dealer_hand.add_card(deck.deal())
        dealer_hand.adjust_for_aces()

        #take initial bet, show cards
        print("The hand will start now.")

        take_bet(p.chips)

        #show some cards prompt for decision
        show_some(player_hand, dealer_hand)
        double_option(p.chips)

        #playing refers to when the game decisions are still up to player
        playing = True

        while playing: 
            #prompt user for decision and show cards 
            while True: 
                x = input("Hit or Stand? Enter [h] for hit or [s] to stand: ")
                if x[0].lower() == 'h':
                    hit(deck,player_hand)
                    show_some(player_hand,dealer_hand)
                    if player_hand.value > 21:
                        player_busts(player_hand, dealer_hand, p.chips)
                        playing = False
                        break
                elif x[0].lower() == 's':
                        print("Player stands it's the dealer's turn now.")
                        playing = False
                        break
                else: 
                    print("Sorry, the input provide was not a proper response. Enter 'h' or 's' to make your choice. ")
                    continue
        if player_hand.value <=21: 
            while dealer_hand.value < 17: #soft 17 rule. 
                hit(deck, dealer_hand)
            show_all(player_hand, dealer_hand)

            #end of game scenarios 
            if dealer_hand.value > 21: 
                dealer_busts(player_hand, dealer_hand, p.chips)
            elif dealer_hand.value > player_hand.value:
                dealer_wins(player_hand, dealer_hand, p.chips)
            elif dealer_hand.value < player_hand.value:
                player_wins(player_hand, dealer_hand, p.chips)
            else: #push
                push(player_hand,dealer_hand)

        #inform the player of remaining chips & prompt new game. 
        print(f"\n Player {p.name} total chips are now at : {p.chips.total}")
        new_game = input("Would you like to play another hand ? y/n: ")
        if new_game[0].lower() == 'y':
            continue
        else: 
            print("Thanks for playing! The game session has ended. ")
            break