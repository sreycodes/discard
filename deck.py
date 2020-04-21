import random
from card import Card, Suit

class Deck:

    def __init__(self, max_rank, value_order=None, shuffle=True):
        self.cards = []
        self.max_rank = max_rank #Hyper Parameter
        self.seeds = list(range(1000)) #Can make 1000 different deck configurations
        random.shuffle(self.seeds)
        self.shuffle_count = 0
        self.populate_deck(value_order)
        if shuffle:
            self.shuffle_deck()

    def populate_deck(self, value_order):
        order = value_order if value_order is not None else list(range(1, self.max_rank + 1)) * 4
        rank_suit = [[s for s in Suit] for r in list(range(self.max_rank))]
        for val in order:
            suit = rank_suit[val - 1].pop()
            self.cards.append(Card(val, suit))

    def shuffle_deck(self):
        seed = self.seeds[self.shuffle_count]
        self.shuffle_count += 1
        random.shuffle(self.cards)

    def sort_deck(self):
        self.cards = sorted(self.cards)