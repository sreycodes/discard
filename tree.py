from game import Game
from game import Round
import copy
import string
import random

class Node:

    def __init__(self, ms, rs_no, rs_hand, opp_no, opp_hand, level, cp=[]):

        self.ms = ms
        self.turn_no = rs_no
        self.turn_hand = rs_hand
        self.opp_no = opp_no
        self.opp_hand = opp_hand
        self.cp = cp
        self.children = []
        self.l = level
        self.id = ''.join(random.choices(string.ascii_uppercase + string.digits, k = 5))

    def __str__(self):
        return self.id + ' Player ' + str(self.turn_no) + ' with hand ' + str(self.turn_hand) + \
            ' Player ' + str(self.opp_no) + ' with hand ' + str(self.opp_hand) + ' - ' + str(self.cp)

    def check_terminal(self):
        return len(self.turn_hand) == 0 or len(self.opp_hand) == 0

    def check_round_over(self):
        current_sum = sum([card.value for card in self.cp])
        cannot_play = True
        for turn_card, opp_card in zip(self.turn_hand, self.opp_hand):
            if current_sum + turn_card.value <= self.ms or current_sum + opp_card.value <= self.ms:
                cannot_play = False
                break
        return cannot_play

    def print(self, appender):
        print(appender + ' Player ' + str(self.turn_no) + ' with hand ' + str(self.turn_hand) + ' - ' + str(self.cp))
        for c in self.children:
            c.print(appender + ' ')

    def get_winner(self):
        if len(self.turn_hand) == 0:
            return self.turn_no
        elif len(self.opp_hand) == 0:
            return self.opp_no
        else:
            print('Not a terminal node - no one won!')
            print(str(self.cp) + ' ' + str(self.turn_hand) + ' ' + str(self.opp_hand))
            return None

class GameTree:

    def __init__(self, game):
        self.root = Node(game.max_sum, game.round_starter.player_no, game.round_starter.hand, 
            game.return_opponent(game.round_starter).player_no, 
            game.return_opponent(game.round_starter).hand, 0)
        self.root = self.make_tree(self.root)

    def make_tree(self, node):
        if node.check_terminal():
            return node
        else:
            # print(node.l * ' ' + str(node))
            if node.check_round_over():
                child_node = Node(node.ms, node.opp_no, node.opp_hand, node.turn_no, node.turn_hand, node.l + 1)
                child_node = self.make_tree(child_node)
                node.children.append(child_node)
            else:
                current_sum = sum([card.value for card in node.cp])
                for value in set([turn_c.value for turn_c in node.turn_hand]):
                    # print(card)
                    nth = node.turn_hand[:]
                    ncp = node.cp[:]
                    if current_sum + value <= node.ms:
                        sc = False
                        card = next(iter([turn_c for turn_c in node.turn_hand if turn_c.value == value]))
                        nth.remove(card)
                        ncp += [card]
                        opp_pc = sum([1 if node.ms - current_sum - value - opp_c.value >= 0 else 0 for opp_c in node.opp_hand])
                        if opp_pc > 0:
                            child_node = Node(node.ms, node.opp_no, node.opp_hand, node.turn_no, nth, node.l + 1, ncp)
                        else:
                            child_node = Node(node.ms, node.turn_no, nth, node.opp_no, node.opp_hand, node.l + 1, ncp)
                        # print(ncp)
                        child_node = self.make_tree(child_node)
                        node.children.append(child_node)
            return node

    def get_winners(self, node):
        if len(node.children) == 0:
            return [node.get_winner()]
        else:
            winners = []
            for child in node.children:
                for winner in self.get_winners(child):
                    winners.append(winner)
            return winners

    def check_if_deterministic(self):
        # print(self.game)
        w = self.get_winners(self.root)
        return len(set(w)) == 1



if __name__ == '__main__':
    g = Game(5,5)
    t = GameTree(g)
    print(g)
    # t.root.print('')
    print(t.check_if_deterministic())



            




