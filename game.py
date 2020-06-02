from player import Player
from deck import Deck

class Round:

    def __init__(self, max_sum, first_player, other_player):
        self.cards_played = []
        self.max_sum = max_sum
        self.fp = first_player
        self.op = other_player
        self.turn = self.fp

    def __str__(self):
        return 'Round ' + self.id + ' at turn ' + str(self.turn) + ' - ' + str(self.cards_played) 

    def return_opponent(self, player):
        return self.op if player == self.fp else self.fp

    def check_if_over(self):
        current_sum = sum([card.value for card in self.cards_played])

        if (self.fp.hand_empty() or self.op.hand_empty()) or (self.fp.cannot_play(self.max_sum, current_sum) and self.op.cannot_play(self.max_sum, current_sum)):
            # print('Player ', self.fp.player_no, ' Hand', self.fp.hand)
            # print('Player ', self.op.player_no, ' Hand', self.op.hand)
            return True

        # print('Current Sum = ', current_sum)
        return False

    def play_turn(self):
        card_played = self.turn.play(self.cards_played, self.max_sum, self.return_opponent(self.turn).hand, self.turn.strategy)
        if card_played is not None:
            # print('Player ', self.turn.player_no, ' played ', card_played)
            self.cards_played.append(card_played)
        self.turn = self.return_opponent(self.turn)

    def run_round(self):
        print('\nNew round started')
        while(not self.check_if_over()):
            self.play_turn()
            print('Cards played - ', self.cards_played)
        print('Round ended\n')
        return self.return_opponent(self.turn)

class Game:

    def __init__(self, max_rank, max_sum, strategy_one = "rand", strategy_two = "rand", custom_deck=None):
        self.player1 = Player(1, strategy_one)
        self.player2 = Player(2, strategy_two)

        #Hyper parameters
        self.max_rank = max_rank
        self.max_sum = max_sum

        if custom_deck is None:
            self.deck = Deck(self.max_rank)
        else:
            self.deck = custom_deck
        self.player1.hand_cards(self.deck.cards[::2])
        self.player2.hand_cards(self.deck.cards[1::2])

        self.round_starter = self.player1

    def __str__(self):
        return 'Game(' + str(self.max_rank) + ', ' + str(self.max_sum) + ') started with\n' + 'Player 1 - ' + str(self.player1.hand) + '\nPlayer 2 - ' + str(self.player2.hand)

    def return_opponent(self, player):
        return self.player2 if player == self.player1 else self.player1

    def check_if_over(self):
        return len(self.player1.hand) == 0 or len(self.player2.hand) == 0

    def return_winner(self):
        if len(self.player1.hand) == 0:
            return self.player1
        if len(self.player2.hand) == 0:
            return self.player2
        # print('No one has won the game yet!')
        return None

    def run_game(self):
        print('Game started')
        rounds = []
        while(not self.check_if_over()):
            r = Round(self.max_sum, self.round_starter, self.return_opponent(self.round_starter))
            self.round_starter = r.run_round()
            rounds.append(r)
        print('Game over')
        winner = self.return_winner()
        print('player ', winner.player_no, ' won')
        return winner, rounds

if __name__ == '__main__':
    # Current strategies: "min", "max", "rand"
    # Strategies can be found and made in player.py play()
    custom_deck = Deck(3, [1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3], shuffle=False)
    # print(custom_deck.cards)
    player_no = input("Enter 1 to play as player 1 and 2 as player 2")
    if player_no == 1:
        g = Game(3, 7, "user", "sim_round")#, custom_deck) # Hyper parameters
    else:
        g = Game(3, 7, "smart", "user")#, custom_deck) # Hyper parameters
    print(g)
    g.run_game()
