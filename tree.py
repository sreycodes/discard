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
        self.winner = opp_no
        self.possible_winners = []

    def __str__(self):
        return self.id + ' Player ' + str(self.turn_no) + ' with hand ' + str(self.turn_hand) + \
            ' Player ' + str(self.opp_no) + ' with hand ' + str(self.opp_hand) + ' - ' + str(self.cp)

    def check_terminal(self):
        return len(self.turn_hand) == 0 or len(self.opp_hand) == 0

    def check_round_over(self):
        current_sum = sum([card.value for card in self.cp])
        # print(current_sum, self.ms)
        cannot_play = True
        for turn_card in self.turn_hand:
            # print(turn_card)
            if current_sum + turn_card.value <= self.ms:
                cannot_play = False
                break
        return cannot_play

    def print(self, appender):
        print(appender + ' Player ' + str(self.turn_no) + ' with hand ' + str(self.turn_hand) + ' - ' + str(self.cp) + ' winners - ' + str(self.possible_winners))
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

    def __init__(self, ms, rs_no, rs_hand, opp_no, opp_hand, make_tree = False):
        self.root = Node(ms, rs_no, rs_hand, opp_no, opp_hand, 0)
        if make_tree:
            self.root = self.make_tree(self.root)

    def is_tree_made(self):
        return len(self.root.children) > 0

    def make_round_tree(self, node):
        if node.check_round_over():
            node.winner = node.turn_no
            node.possible_winners.append(node.turn_no)
            return [node], node.turn_no
        else:
            leaves = []
            current_sum = sum([card.value for card in node.cp])
            for value in set([turn_c.value for turn_c in node.turn_hand]):
                # print(card)
                nth = node.turn_hand[:]
                ncp = node.cp[:]
                if current_sum + value <= node.ms:
                    card = next(iter([turn_c for turn_c in node.turn_hand if turn_c.value == value]))
                    nth.remove(card)
                    ncp += [card]
                    opp_pc = sum([1 if node.ms - current_sum - value - opp_c.value >= 0 else 0 for opp_c in node.opp_hand])
                    if opp_pc > 0:
                        child_node = Node(node.ms, node.opp_no, node.opp_hand, node.turn_no, nth, node.l + 1, ncp)
                    else:
                        child_node = Node(node.ms, node.turn_no, nth, node.opp_no, node.opp_hand, node.l + 1, ncp)
                    # print(ncp)
                    node.children.append(child_node)
                    l, w = self.make_round_tree(child_node)
                    if w == node.turn_no:
                        node.winner = node.turn_no
                    for leaf in l:
                        leaves.append(leaf)
                    for winner in child_node.possible_winners:
                        node.possible_winners.append(winner)
            return leaves, node.winner

    def choose_card_for_round(self, ms, yp_no, yp_hand, opp_no, opp_hand):
        rs_node = Node(ms, yp_no, yp_hand, opp_no, opp_hand, 0, [])
        leaves, winner = self.make_round_tree(rs_node)
        if winner == opp_no: #whatever you do you lose
            print('No matter what you play you lose')
            return yp_hand[0] #any card really
        else: #Choose child with most victories
            winner_nodes = [x for x in rs_node.children if x.winner == yp_no]
            # rs_node.print('')
            # print(rs_node.check_round_over())
            most_probable_winner_node = winner_nodes[0]
            num_wins = len([x for x in most_probable_winner_node.possible_winners if x == yp_no])
            for child in winner_nodes:
                nw = len([x for x in child.possible_winners if x == yp_no])
                # print(child.possible_winners, child.cp)
                if nw > num_wins:
                    num_wins = nw
                    most_probable_winner_node = child
            # print('Best card to play - ' + str(most_probable_winner_node.cp[0]))
            return most_probable_winner_node.cp[0]

    def make_tree(self, node):
        if node.check_terminal():
            return node
        else:
            leaves, round_winner = self.make_round_tree(node)
            for leaf in leaves:
                next_node = Node(leaf.ms, leaf.turn_no, leaf.turn_hand, leaf.opp_no, leaf.opp_hand, leaf.l + 1, [])
                next_node = self.make_tree(next_node)
                leaf.children.append(next_node)
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
        if not self.is_tree_made():
            self.root = self.make_tree(self.root)
        w = self.get_winners(self.root)
        return len(set(w)) == 1



if __name__ == '__main__':
    self.deck = Deck(self.max_rank)
    t = GameTree(3, 1, self.deck.cards[::2], 2, self.deck.cards[1::2], True)
    t.root.print('')
    print(t.check_if_deterministic())



            




