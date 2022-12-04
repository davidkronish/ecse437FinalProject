from cgi import test
from importlib.util import find_spec
import pytest

from blackjack.Hand import Hand
from blackjack.chips import chips
from blackjack.card import card
from blackjack.Deck import Deck
from blackjack.Player import Player
from blackjack.gamefunctions import input_chips, take_bet, double_option, hit, show_some, show_all, player_wins_off_blackjack, player_busts, player_wins, dealer_busts, dealer_wins, push

#unit tests
#cards
def test_card_invalid():
    with pytest.raises(Exception) as exc_info:
        card('Hearts', 'Joker')
    assert exc_info.value.args[0] == "The suit or rank is not valid entry."

def test_card_valid():
    try: 
        c = card('Hearts', 'Five')
    except Exception as exc:
        assert False, f" Creation of card : {c.__str__()} creates exception."
    
def test_deck_number_of_cards_in_deck():
    d = Deck()
    print(d.__str__())
    assert len(d.deck) == 260

#deck
def test_deck_deal():
    d = Deck()
    test_card = card('Hearts', 'Five')
    d.deck.append(test_card)
    return_card = d.deal()
    assert return_card == test_card

def test_deck_shuffle():
    d = Deck()
    first_5 = d.deck[0:5]
    d.shuffle()
    assert d.deck[0:5] is not first_5

#hands
def test_hand_adds_value():
    test_card_1 = card('Hearts', 'Ten')
    test_card_2 = card('Clubs', 'Five')
    h = Hand()
    h.add_card(test_card_1)
    h.add_card(test_card_2)
    assert len(h.cards) == 2
    assert test_card_1, test_card_2 in h.cards
    assert h.value == 15

def test_hand_adds_aces():
    test_card_1 = card('Hearts', 'Ace')
    test_card_2 = card('Clubs', 'Five')
    h = Hand()
    h.add_card(test_card_1)
    h.add_card(test_card_2)
    assert len(h.cards) == 2
    assert test_card_1, test_card_2 in h.cards
    assert h.aces == 1


def test_hand_adjust_for_aces():
    test_card_1 = card('Hearts', 'Ace')
    test_card_2 = card('Clubs', 'Two')
    test_card_3 = card('Spades', 'Ace')
    h = Hand()
    h.add_card(test_card_1)
    h.add_card(test_card_2)
    h.add_card(test_card_3)
    assert h.value == 24
    h.adjust_for_aces()
    assert h.value == 14
    assert h.aces == 1

#player & chips

def test_player_and_chip_creation():
    p = Player("Test Player", 1000)
    assert p.chips.__class__ == chips
    assert p.chips.total == 1000
    assert p.__str__() == "Player Test Player has a total of 1000 chips."


def test_player_wins_bet():
    p = Player("Test Player", 1000)
    p.chips.bet = 50
    assert p.chips.total == 1000
    p.chips.win_bet()
    assert p.chips.total == 1050


def test_player_loses_bet():
    p = Player("Test Player", 1000)
    p.chips.bet = 50
    assert p.chips.total == 1000
    p.chips.lose_bet()
    assert p.chips.total == 950

def test_player_wins_blackjack():
    p = Player("Test Player", 1000)
    p.chips.bet = 50
    assert p.chips.total == 1000
    p.chips.win_blackjack()
    assert p.chips.total == 1075


#integration tests 