# -*- coding: utf-8 -*-
# @Author: boyac
# @Date:   2016-08-20 11:41:27
# @Last Modified by:   boyac
# @Last Modified time: 2016-08-20 11:55:28

import string
import random
#import enchant

#d = enchant.Dict("en_US")

''' 
Question: 
Assign a=1, b=b,...,z=26. Find an 8 letter word whose sum is less than 50.
'''
with open("en_word.txt") as word_file:
    english_words = set(word.strip().lower() for word in word_file)


def convert_num(word):
	num = [ord(char) - 96 for char in word.lower()]
	return num



if __name__ == '__main__':
	for i in english_words:
		if len(convert_num(i)) == 8 and sum(convert_num(i)) < 50:
			print convert_num(i), i


'''
Result:
[1, 3, 1, 4, 5, 13, 9, 3] academic
[1, 3, 1, 4, 5, 13, 9, 1] academia
[2, 5, 1, 3, 15, 14, 5, 4] beaconed
[3, 12, 1, 13, 2, 1, 11, 5] clambake
[5, 13, 2, 5, 4, 4, 5, 4] embedded
[2, 5, 1, 4, 12, 9, 11, 5] beadlike
[2, 9, 14, 4, 1, 2, 12, 5] bindable
[2, 1, 4, 7, 5, 18, 5, 4] badgered
[4, 5, 9, 3, 9, 4, 1, 12] deicidal
[4, 5, 6, 1, 3, 9, 14, 7] defacing
[2, 5, 1, 18, 1, 2, 12, 5] bearable
[1, 2, 9, 4, 1, 14, 3, 5] abidance
[2, 1, 3, 11, 2, 5, 14, 4] backbend
[6, 5, 5, 4, 2, 1, 7, 19] feedbags
[1, 13, 9, 3, 1, 2, 12, 5] amicable
[1, 2, 1, 20, 1, 2, 12, 5] abatable
[2, 1, 3, 3, 1, 18, 1, 20] baccarat
[4, 10, 5, 12, 12, 1, 2, 1] djellaba
[2, 5, 1, 3, 8, 9, 14, 7] beaching
[2, 1, 12, 1, 14, 3, 5, 4] balanced
[16, 5, 3, 3, 1, 2, 12, 5] peccable
[2, 15, 12, 4, 6, 1, 3, 5] boldface
[3, 1, 2, 2, 1, 7, 5, 4] cabbaged
[3, 1, 3, 8, 5, 20, 5, 4] cacheted
[2, 1, 3, 11, 4, 1, 20, 5] backdate
[2, 1, 3, 11, 8, 1, 14, 4] backhand
[8, 1, 12, 6, 2, 5, 1, 11] halfbeak
[5, 3, 8, 9, 4, 14, 1, 5] echidnae
[4, 5, 3, 5, 1, 19, 5, 4] deceased
[16, 1, 3, 9, 6, 9, 3, 1] pacifica
[4, 5, 1, 4, 6, 1, 12, 12] deadfall
[8, 1, 12, 6, 2, 1, 3, 11] halfback
[3, 1, 12, 12, 1, 2, 12, 5] callable
[3, 1, 2, 1, 12, 12, 5, 4] caballed
[16, 1, 12, 5, 6, 1, 3, 5] paleface
[3, 8, 9, 3, 1, 14, 5, 4] chicaned
[3, 15, 3, 11, 1, 4, 5, 4] cockaded
[6, 1, 3, 5, 1, 2, 12, 5] faceable
[2, 12, 1, 14, 3, 8, 5, 4] blanched
[4, 5, 6, 9, 1, 14, 3, 5] defiance
[3, 1, 18, 1, 16, 1, 3, 5] carapace
[2, 5, 4, 1, 21, 2, 5, 4] bedaubed
[2, 9, 18, 4, 3, 1, 7, 5] birdcage
[6, 1, 12, 12, 2, 1, 3, 11] fallback
[8, 1, 18, 4, 2, 1, 3, 11] hardback
[2, 5, 5, 2, 18, 5, 1, 4] beebread
[2, 1, 8, 1, 13, 9, 1, 14] bahamian
[1, 3, 3, 5, 4, 9, 14, 7] acceding
[2, 5, 3, 8, 1, 13, 5, 12] bechamel
[2, 1, 14, 4, 1, 7, 5, 4] bandaged
[2, 5, 3, 1, 12, 13, 5, 4] becalmed
[3, 1, 13, 2, 15, 4, 9, 1] cambodia
[8, 5, 1, 4, 12, 1, 14, 4] headland
[4, 5, 7, 18, 1, 4, 5, 4] degraded
[2, 5, 4, 1, 13, 14, 5, 4] bedamned
[4, 9, 1, 4, 5, 13, 5, 4] diademed
[2, 12, 5, 1, 3, 8, 5, 4] bleached
[2, 5, 4, 5, 3, 11, 5, 4] bedecked
[4, 5, 1, 4, 5, 14, 5, 4] deadened
[4, 5, 1, 6, 5, 14, 5, 4] deafened
[8, 5, 1, 4, 1, 3, 8, 5] headache
[2, 12, 1, 2, 2, 9, 14, 7] blabbing
[4, 5, 6, 5, 3, 1, 20, 5] defecate
[6, 12, 1, 13, 2, 5, 5, 4] flambeed
[18, 5, 1, 4, 1, 2, 12, 5] readable
[1, 3, 3, 15, 12, 1, 4, 5] accolade
[2, 1, 12, 12, 1, 4, 9, 3] balladic
[2, 5, 4, 4, 1, 2, 12, 5] beddable
[3, 1, 12, 3, 9, 6, 9, 3] calcific
[1, 4, 1, 13, 1, 14, 3, 5] adamance
[8, 1, 3, 9, 5, 14, 4, 1] hacienda
[3, 1, 6, 6, 5, 9, 14, 5] caffeine
[2, 5, 7, 7, 1, 18, 5, 4] beggared
[3, 1, 12, 3, 1, 18, 9, 1] calcaria
[2, 1, 2, 2, 12, 9, 14, 7] babbling
[2, 5, 14, 4, 1, 2, 12, 5] bendable
[1, 2, 4, 9, 3, 1, 20, 5] abdicate
[2, 12, 1, 13, 1, 2, 12, 5] blamable
[4, 5, 1, 20, 8, 2, 5, 4] deathbed
[2, 1, 9, 12, 1, 2, 12, 5] bailable
[2, 1, 12, 4, 8, 5, 1, 4] baldhead
[2, 5, 1, 14, 2, 1, 12, 12] beanball
[3, 18, 9, 2, 2, 1, 7, 5] cribbage
[3, 1, 12, 1, 2, 1, 19, 8] calabash
[16, 1, 3, 11, 1, 7, 5, 4] packaged
[2, 5, 8, 5, 1, 4, 5, 4] beheaded
[8, 5, 1, 4, 7, 5, 1, 18] headgear
[2, 1, 18, 5, 8, 5, 1, 4] barehead
[3, 1, 19, 3, 1, 2, 5, 12] cascabel
[10, 1, 2, 2, 5, 18, 5, 4] jabbered
[3, 1, 4, 5, 14, 3, 5, 4] cadenced
[8, 1, 18, 4, 8, 5, 1, 4] hardhead
[2, 1, 7, 7, 1, 7, 5, 19] baggages
[3, 5, 14, 20, 5, 18, -57, 19] center's
[1, 2, 2, 1, 20, 9, 1, 12] abbatial
[8, 5, 1, 4, 2, 1, 14, 4] headband
[8, 5, 1, 12, 1, 2, 12, 5] healable
[2, 9, 4, 4, 1, 2, 12, 5] biddable
[3, 1, 14, 14, 1, 2, 9, 3] cannabic
[4, 21, 14, 4, 5, 5, -57, 19] dundee's
[13, 5, 4, 9, 3, 1, 9, 4] medicaid
[3, 8, 9, 12, 4, 2, 5, 4] childbed
[1, 13, 2, 9, 1, 14, 3, 5] ambiance
[3, 1, 14, 3, 5, 12, 5, 4] canceled
[9, 13, 2, 5, 4, 4, 5, 4] imbedded
[1, 2, 2, 1, 3, 9, 5, 19] abbacies
[2, 5, 5, 6, 3, 1, 11, 5] beefcake
[18, 5, 1, 3, 3, 5, 4, 5] reaccede
[2, 1, 18, 5, 2, 1, 3, 11] bareback
[2, 1, 14, 11, 1, 2, 12, 5] bankable
[6, 5, 5, 4, 2, 1, 3, 11] feedback
[2, 1, 3, 11, 16, 1, 3, 11] backpack
[6, 12, 5, 1, 2, 1, 14, 5] fleabane
[2, 1, 4, 9, 14, 1, 7, 5] badinage
[1, 3, 9, 4, 8, 5, 1, 4] acidhead
[2, 1, 3, 11, 1, 3, 8, 5] backache
[4, 5, 6, 5, 14, 4, 5, 4] defended
[11, 1, 2, 2, 1, 12, 1, 8] kabbalah
[11, 1, 2, 2, 1, 12, 1, 19] kabbalas
[3, 1, 19, 3, 1, 4, 5, 4] cascaded
[1, 6, 6, 9, 1, 14, 3, 5] affiance
[3, 1, 2, 2, 1, 7, 5, 19] cabbages
[4, 5, 1, 4, 2, 5, 1, 20] deadbeat
[3, 1, 4, 9, 12, 12, 1, 3] cadillac
[3, 1, 14, 1, 4, 9, 1, 14] canadian
[2, 9, 12, 1, 2, 9, 1, 12] bilabial
[2, 18, 5, 1, 3, 8, 5, 4] breached
[2, 5, 1, 20, 1, 2, 12, 5] beatable
[2, 5, 14, 5, 6, 9, 3, 5] benefice
[3, 1, 2, 2, 1, 12, 1, 19] cabbalas
[4, 5, 1, 4, 8, 5, 1, 4] deadhead
[3, 1, 12, 12, 2, 1, 3, 11] callback
[6, 5, 5, 4, 1, 2, 12, 5] feedable
[4, 5, 9, 6, 9, 3, 1, 12] deifical
[3, 1, 2, 2, 1, 12, 1, 8] cabbalah
'''
