import sys
class chips: 
    def __init__(self, total=100) -> None:
        self.total = total 
        self.bet = 0

    def win_bet(self):
        self.total += self.bet

    def lose_bet(self):
        self.total -= self.bet
    
    def win_blackjack(self):
        self.total += self.bet*1.5