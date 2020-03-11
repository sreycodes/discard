import random
from card import Card, Suit

class Deck:

    def __init__(self, max_rank, rank_order=None, shuffle=True):
        self.cards = []
        self.max_rank = max_rank #Hyper Parameter
        self.seeds = list(range(1000)) #Can make 1000 different deck configurations
        random.shuffle(self.seeds)
        self.shuffle_count = 0
        self.populate_deck(rank_order)
        if shuffle:
            self.shuffle_deck()

    def populate_deck(self, rank_order):
        order = rank_order if rank_order != None else range(1, self.max_rank + 1)
        for rank in order:
            for suit in Suit:
                self.cards.append(Card(rank, suit))

    def shuffle_deck(self):
        seed = self.seeds[self.shuffle_count]
        self.shuffle_count += 1
        random.shuffle(self.cards)

    def sort_deck(self):
        self.cards = sorted(self.cards)