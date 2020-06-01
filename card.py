from enum import Enum
from functools import total_ordering

class Suit(Enum):
    CLUBS = 1
    DIAMONDS = 2
    HEARTS = 3
    SPADES = 4

@total_ordering
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
        suit_to_str = ['C', 'D','H', 'S']
        return suit_to_str[self.suit.value - 1] + str(self.rank)

    def __repr__(self):
        suit_to_str = ['C', 'D','H', 'S']
        return suit_to_str[self.suit.value - 1] + str(self.rank)

    def __cmp__(self, obj):
        return self.value - obj.value

    def __lt__(self, other):
        return self.value < other.value

    @classmethod
    def from_str(cls, s):
        try:
            str_to_suit = {'H': Suit.HEARTS, 'C': Suit.CLUBS, 'D': Suit.DIAMONDS, 'S': Suit.SPADES}
            suit = str_to_suit[s[0]]
            rank = int(s[1:])
            return cls(rank, suit), None
        except Exception as e:
            return None, e
