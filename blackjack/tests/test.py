import pytest

from blackjack.Hand import Hand

def test_hand():
    h = Hand()
    h.value = 5
    assert h.value == 6
