from player import Player
from deck import Deck

class Round:

    def __init__(self, max_sum, first_player, other_player):
        self.cards_played = []
        self.max_sum = max_sum
        self.fp = first_player
        self.op = other_player
        self.turn = self.fp

    def return_opponent(self, player):
        return self.op if player == self.fp else self.fp

    def check_if_over(self):
        current_sum = sum([card.value for card in self.cards_played])

        if self.fp.cannot_play(self.max_sum, current_sum) and self.op.cannot_play(self.max_sum, current_sum):
            print(self.fp.player_no, ' Player Hand', self.fp.hand)
            print(self.op.player_no, ' Player Hand', self.op.hand)
            return True

        print('Current Sum = ', current_sum)
        return False

    def play_turn(self):
        card_played = self.turn.play(self.cards_played, self.max_sum, self.op.hand, "random")
        if card_played != None:
            print('Player ', self.turn.player_no, ' played ', card_played)
            self.cards_played.append(card_played)
        self.turn = self.return_opponent(self.turn)

    def run_round(self):
        print('New round started')
        while(not self.check_if_over()):
            self.play_turn()
            print('Cards played - ', self.cards_played)
        print('Round ended')
        return self.return_opponent(self.turn)


class Game:

    def __init__(self, max_rank, max_sum):
        self.player1 = Player(1)
        self.player2 = Player(2)

        #Hyper parameters
        self.max_rank = max_rank
        self.max_sum = max_sum

        self.deck = Deck(self.max_rank)
        self.player1.hand_cards(self.deck.cards[::2])
        self.player2.hand_cards(self.deck.cards[1::2])

        self.round_starter = self.player1
        print(self.player1)
        print(self.player2)

    def return_opponent(self, player):
        return self.player2 if player == self.player1 else self.player1

    def check_if_over(self):
        return len(self.player1.hand) == 0 or len(self.player2.hand) == 0

    def return_winner(self):
        if len(self.player1.hand) == 0:
            return self.player1
        if len(self.player2.hand) == 0:
            return self.player2
        print('No one has won the game yet!')
        return None

    def run_game(self):
        print('Game started')
        while(not self.check_if_over()):
            r = Round(self.max_sum, self.round_starter, self.return_opponent(self.round_starter))
            self.round_starter = r.run_round()
        print('Game over')
        winner = self.return_winner()
        print(winner.player_no, ' player won')

if __name__ == '__main__':
    g = Game(4, 11) # Hyper parameters
    g.run_game()