# -*- coding: utf-8 -*-
# @Author: boyac
# @Date:   2016-08-25 12:16:07
# @Last Modified by:   boyac
# @Last Modified time: 2016-08-25 12:53:16

'''
Questions: 
You have two decks of cards: a 52 card deck (26 black, 26 red) 
and a 26 card deck (13 black, 13 red). You randomly draw two cards and 
win if both are the same color. Which deck would you prefer? 
What if the 26 card deck was randomly drawn from 
the 52 card deck? Which deck would you prefer then?
'''

import random
from collections import Counter
import __future__
import math

new_deck = []
for i in range(26):
	new_deck.append(random.choice('RB'))


if __name__ == '__main__':
	print Counter(new_deck)
	# Counter({'B': 16, 'R': 10})
	'''I will choose the 3rd deck, it gives higher probability of winning'''
