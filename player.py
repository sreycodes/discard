import random

class Player:

    def __init__(self, player_no):
        self.player_no = player_no
        self.hand = []

    def __eq__(self, other):
        """Overrides the default implementation"""
        if isinstance(other, Player):
            return self.player_no == other.player_no
        return False

    def __ne__(self, other):
        """Overrides the default implementation (unnecessary in Python 3)"""
        return not self.__eq__(other)

    def __str__(self):
        return 'Player ' + str(self.player_no) + ' - ' + str(self.hand)

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

    def cannot_play(self, max_sum, current_sum):
        if len(self.hand) == 0:
            return True
        cannot_play = True
        for card in self.hand:
            if current_sum + card.value <= max_sum:
                cannot_play = False
                break
        return cannot_play

    def play(self, cards_played, max_sum, other_player_hand, algo_name):
        # Write algo to decide card and call play_cardn

        current_sum = sum([card.value for card in cards_played])
        if self.cannot_play(max_sum, current_sum):
            return None

        if algo_name == "random":
            index = 0
            card = self.hand[index]
            while(card.value + current_sum > max_sum):
                index += 1
                card = self.hand[index]
            return self.play_card(card)

        return None