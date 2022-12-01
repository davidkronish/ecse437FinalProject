import random
from blackjack.card import card

class Deck(object): 
    suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
    ranks = ('Two', 'Three','Four','Five','Six','Seven','Eight','Nine','Ten','Jack','Queen','King','Ace')
    
    def __init__(self) -> None:
        self.deck = []
        #use 5 decks add them to total deck
        for _ in range(5):
            for suit in self.suits:
                for rank in self.ranks:
                    self.deck.append(card(suit,rank))
                
    def __str__(self) -> str:
        deck_comp = ''
        for card in self.deck:
            deck_comp += '\n' + card.__str__()
        return "The deck has: "+deck_comp
        
    def shuffle(self):
        random.shuffle(self.deck)

    def deal(self):
        single_card = self.deck.pop()
        return single_card
