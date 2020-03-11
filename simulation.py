from game import Game
from itertools import product
from deck import Deck

def run_simulations(max_rank_list, max_sum_list, strategy_one_list, strategy_two_list, custom_deck_list):

    # Assert all lists have same length
    assert len(max_rank_list) == len(max_sum_list), "Length of MRL and MSL not equal"
    assert len(strategy_one_list) == len(max_sum_list), "Length of S1L and MSL not equal"
    assert len(strategy_one_list) == len(strategy_two_list), "Length of S1L and S2L not equal"
    assert len(strategy_two_list) == len(custom_deck_list), "Length of S2L and CDL not equal"

    n = len(max_rank_list)
    winners = []
    round_info = []
    p1wins, p2wins = 0, 0

    for i in range(n):
        mr = max_rank_list[i]
        ms = max_sum_list[i]
        s1 = strategy_one_list[i]
        s2 = strategy_two_list[i]
        cd = custom_deck_list[i]
        g = Game(mr, ms, s1, s2, cd)
        w, r = g.run_game()
        winners.append(w)
        round_info.append(r)
        if w == g.player1:
            p1wins += 1
        else:
            p2wins += 1

    print(n, ' games played')
    print('Player 1 won ', p1wins * 100 / n, ' percent of the time')
    print('Player 2 won ', p2wins * 100 / n, ' percent of the time')

    return winners, round_info

def grid_simulations(max_rank_list, max_sum_list, strategy_one_list, strategy_two_list, custom_deck_list):

    game_info = []
    p1wins, p2wins = 0, 0
    n = 0

    for (mr, ms, s1, s2, cd) in product(max_rank_list, max_sum_list, strategy_one_list, strategy_two_list, custom_deck_list):
        g = Game(mr, ms, s1, s2, cd)
        w, r = g.run_game()
        game_info.append({"game": g, "winner": w, "round_info": r})
        if w == g.player1:
            p1wins += 1
        else:
            p2wins += 1
        n += 1

    print(n, ' games played')
    print('Player 1 won ', p1wins * 100 / n, ' percent of the time')
    print('Player 2 won ', p2wins * 100 / n, ' percent of the time')

    return game_info

if __name__ == '__main__':
    mrl = [4, 5]
    msl = [11, 16]
    s1l = ["min", "max"]
    s2l = s1l
    cdl = [None, Deck(mrl[1], shuffle=False)]

    run_simulations(mrl, msl, s1l, s2l, cdl)
    # grid_simulations(mrl, msl, s1l, s2l, cdl)



