import random
from card import Card
from tree import GameTree

class Player:

    def __init__(self, player_no, strategy):
        self.player_no = player_no
        self.strategy = strategy
        self.hand = []

    def __eq__(self, other):
        """Overrides the default implementation"""
        if isinstance(other, Player):
            return self.player_no == other.player_no
        return False

    def __hash__(self):
        return self.player_no

    def __ne__(self, other):
        """Overrides the default implementation (unnecessary in Python 3)"""
        return not self.__eq__(other)

    def __str__(self):
        return 'Player ' + str(self.player_no) + ' with hand - ' + str(self.hand)

    def hand_one_card(self, card):
        self.hand.append(card)

    def hand_cards(self, cards):
        for card in cards:
            self.hand_one_card(card)

    def play_card(self, card):
        self.hand.remove(card)
        return card

    def choose_random_card(self):
        random_index = random.random() * len(self.hand)
        return self.hand[random_index]

    def hand_empty(self):
        return len(self.hand) == 0

    def cannot_play(self, max_sum, current_sum):
        if self.hand_empty():
            return True
        cannot_play = True
        for card in self.hand:
            if current_sum + card.value <= max_sum:
                cannot_play = False
                break
        return cannot_play

    def play(self, cards_played, max_sum, other_player_hand, strategy, game=None):
        # Write algo to decide card and call play_card()

        current_sum = sum([card.value for card in cards_played])
        if self.cannot_play(max_sum, current_sum):
            return None

        if isinstance(strategy, Card):
            return self.play_card(strategy)

        if strategy == "sim_round":
            t = GameTree(max_sum - current_sum, self.player_no, self.hand, self.player_no + 1, other_player_hand)
            return self.play_card(t.choose_card_for_round(max_sum - current_sum, self.player_no, self.hand, self.player_no + 1, other_player_hand))

        if strategy == "rand":
            index = 0
            card = self.hand[index]
            while(card.value + current_sum > max_sum):
                index += 1
                card = self.hand[index]
            return self.play_card(card)

        elif strategy == "smart":
            # play card if can add to max_sum
            for index in range(len(self.hand)):
                if self.hand[index].value + current_sum == max_sum:
                    return self.play_card(self.hand[index])

            # else play max card that doesn't allow other player to win round
            max_valid_card = None
            for i in range(len(self.hand)):
                valid = True
                for j in range(len(other_player_hand)):
                    if self.hand[index].value + other_player_hand[j].value + current_sum == max_sum:
                        valid = False
                if valid:
                    if max_valid_card == None or self.hand[index].value > max_valid_card.value:
                        max_valid_card = self.hand[index]

            if max_valid_card != None:
                return self.play_card(max_valid_card)
            
            # else just play max card
            else:
                max_card = self.hand[0]
                for index in range(len(self.hand)):
                    # if initial card is invalid
                    if max_card.value + current_sum > max_sum:
                        max_card = self.hand[index]
                    if self.hand[index].value > max_card.value and self.hand[index].value + current_sum <= max_sum:
                        max_card = self.hand[index]
                return self.play_card(max_card)

        elif strategy == "min":
            min_card = self.hand[0]
            for index in range(len(self.hand)):
                if self.hand[index].value < min_card.value:
                    min_card = self.hand[index]
            return self.play_card(min_card)

        elif strategy == "max":
            max_card = self.hand[0]
            for index in range(len(self.hand)):
                # if initial card is invalid
                if max_card.value + current_sum > max_sum:
                    max_card = self.hand[index]
                if self.hand[index].value > max_card.value and self.hand[index].value + current_sum <= max_sum:
                    max_card = self.hand[index]
            return self.play_card(max_card)

        else:
            raise Exception('Invalid strategy')

        return None