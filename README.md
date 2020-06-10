# Discard

This was a card game made as a final project for [Applied Combinatorics](https://math.gatech.edu/courses/math/3012) during my semester at Georgia Tech.

## Setup and Instructions

All of the cards from Ace, 2, …, **max_rank** are taken from the deck and distributed randomly amongst two players so that they have the same number of cards in their hands but not necessarily the same number of each rank, e.g. 
max_rank = 4  

    Player 1 hand: A, A, A, 2, 2, 3, 3, 4  
    
    Player 2 hand: A, 2, 2, 3, 3, 4, 4, 4  
    
Players take turns playing one of their cards to the middle, adding on to the cards played before. The values of the middle pile are accumulated. The sequence goes on till none of the players can add a card to the middle without exceeding **max_sum**. At this point the sequence is discarded and the last player to play a card in the sequence starts the next sequence. The player able to play all of their cards first wins.  

The default setup for this game is max_rank = 4 and max_sum = 11.  

To play against the AI with these default settings, just run ```python3 game.py```  

```sim.png``` shows the results of the best strategies coded when they are pitted against each other.
