from enum import Enum

class Suit(Enum):
    CLUBS = 1
    DIAMONDS = 2
    HEARTS = 3
    SPADES = 4

class Card:

    def __init__(self, rank, suit):
        if rank < 1 or rank > 13:
            raise ValueError('Rank must be between 1 and 13 inclusive')
        if not isinstance(suit, Suit):
            raise ValueError('Suit must be of instance Suit/Enum')
        self.rank = rank
        self.suit = suit
        self.value = self.rank

    def __eq__(self, other):
        """Overrides the default implementation"""
        if isinstance(other, Card):
            return self.rank == other.rank and self.suit == other.suit
        return False

    def __ne__(self, other):
        """Overrides the default implementation (unnecessary in Python 3)"""
        return not self.__eq__(other)

    def __str__(self):
        return str(self.suit) + ' ' + str(self.rank)

    def __repr__(self):
        return str(self.suit) + ' ' + str(self.rank)

    def __cmp__(self, obj):
        return self.value - obj.value