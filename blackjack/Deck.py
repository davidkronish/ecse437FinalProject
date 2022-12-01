import random

class Deck(object): 
    suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
    ranks = ('Two', 'Three','Four','Five','Six','Seven','Eight','Nine','Ten','Jack','Queen','King','Ace')
    
    def __init__(self) -> None:
        self.deck = []
        #pick arbitrary number of decks, add them to deck
        for _ in range(random.randint(3,6)):
            for suit in self.suits:
                for rank in self.ranks:
                    self.deck.append(Card(suit,rank))
                
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

class Card:
    def __init__(self,suit,rank) -> None:
        self.suit = suit
        self.rank = rank
    
    def __str__(self) -> str:
        return self.rank+ " of "+self.suit
