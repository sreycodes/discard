from game import Game
from itertools import product
from deck import Deck
import matplotlib.pyplot as plt
import numpy as np

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

    return p1wins, p2wins, winners, round_info

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

def plot_simulations_strategies(strategy_list, max_rank=4, max_sum=11, n_iterations=100):
	# runs n_iterations of games of every permutation of stratetgy 1 vs. strategy 2 in strategy list with constant max_rank,
	# max_sum, and deck, then plots a double bar graph of results
	p1wins_list = []
	p2wins_list = []
	x_labels = []
	N = 0

	mrl = []
	msl = []
	cdl = []
	for n in range(n_iterations):
		mrl.append(max_rank)
		msl.append(max_sum)
		cdl.append(Deck(max_rank))

	for strat_one in strategy_list:
		for strat_two in strategy_list:
			s1l = []
			s2l = []
			for n in range(n_iterations):
				s1l.append(strat_one)
				s2l.append(strat_two)
			results = run_simulations(mrl, msl, s1l, s2l, cdl)
			p1wins_list.append(results[0])
			p2wins_list.append(results[1])
			x_labels.append(strat_one + " vs. " + strat_two)
			N += 1

	indices = np.arange(N)
	width = 0.3

	ax = plt.subplot(111)

	rects1 = ax.barh(indices, p1wins_list, width-0.05, color="r")
	rects2 = ax.barh(indices+width, p2wins_list, width-0.05, color="b")

	ax.set_xlabel("Number of Wins")
	ax.set_yticks(indices+(width/2))
	ax.set_yticklabels(x_labels)
	ax.legend((rects1[0], rects2[0]), ('P1 wins', 'P2 wins'))

	plt.grid(axis='x')
	plt.show()

if __name__ == '__main__':
    mrl = [4, 5]
    msl = [11, 16]
    s1l = ["min", "max"]
    s2l = s1l
    cdl = [None, Deck(mrl[1], shuffle=False)]

    # run_simulations(mrl, msl, s1l, s2l, cdl)
    # grid_simulations(mrl, msl, s1l, s2l, cdl)
    plot_simulations_strategies(strategy_list=["min", "max", "rand"])



