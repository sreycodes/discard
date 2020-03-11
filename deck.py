import random
from card import Card, Suit

class Deck:

    def __init__(self, max_rank):
        self.cards = []
        self.max_rank = max_rank #Hyper Parameter
        self.seeds = list(range(1000)) #Can make 1000 different deck configurations
        random.shuffle(self.seeds)
        self.shuffle_count = 0
        self.populate_deck()
        self.shuffle_deck()

    def populate_deck(self):
        for suit in Suit:
            for rank in range(1, self.max_rank + 1):
                self.cards.append(Card(rank, suit))

    def shuffle_deck(self):
        seed = self.seeds[self.shuffle_count]
        self.shuffle_count += 1
        random.shuffle(self.cards)