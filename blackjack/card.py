class card:
    suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
    ranks = ('Two', 'Three','Four','Five','Six','Seven','Eight','Nine','Ten','Jack','Queen','King','Ace')
    
    def __init__(self,suit,rank) -> None:
        if suit not in self.suits or rank not in self.ranks:
            raise Exception("The suit or rank is not valid entry.") 
        self.suit = suit
        self.rank = rank
    
    def __str__(self) -> str:
        return self.rank+ " of "+self.suit