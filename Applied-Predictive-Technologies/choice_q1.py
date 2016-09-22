# -*- coding: utf-8 -*-
# @Author: boyac
# @Date:   2016-04-04 13:35:31
# @Last Modified by:   boyac
# @Last Modified time: 2016-04-04 13:35:31

import itertools
from choice_feed import Data

class Mission1(Data):
	"""
	calculate utility score
	"""
	def __init__(self):
		pass
	
	# (Pay, Hours, Impact, Opportunity to Learn)
	def people_utility(self):
		for line in self.data_merge():
			if line[1] ==  'Money Grubber':
				yield (10, -1, 4, 2)
			elif line[1] == 'Entrepreneur':
				yield (4, -2, 10, 8)
			elif line[1] == 'Slacker':
				yield (1, -10, 2, 2)
			elif line[1] == 'Academic':
				yield (2, -6, 8, 10)


	def offers_utility(self):
		for line in self.data_merge():
			if line[4] == 'Big Software Firm':
				yield (6, 6, 2, 8)
			elif line[4] == 'Hedge Fund':
				yield (8, 8, 4, 6)
			elif line[4] == 'Investment Bank':
				yield (10, 10, 3, 4)
			elif line[4] == 'Startup':
				yield (4, 8, 10, 8)
			elif line[4] == 'Grad School':
				yield (1, 4, 3, 10)
			#elif line[4] == 'Consulting Firm':  # a guesstimation
			#	yield (7, 10, 3, 8)


	def product_utility(self):
		"""
		Calculate the production of personality_utility_coefficient * offers_utility_coefficient
		"""
		A = self.people_utility()
		B = self.offers_utility()
		while True:
			yield sum([a * b for a, b in itertools.izip(next(A), next(B))])


	def profile(self):
		"""
		Generator profile info for output formation
		"""
		for i in self.data_merge():
			yield i[0]
			yield i[1]
			yield i[0]
			yield i[4]


m = Mission1()
d = Data()
dd = d.data_merge()
mm = m.people_utility()
oo = m.offers_utility()
pp = m.product_utility()
idf = m.profile()

print '{} is a {}, if {} works at {}, the utility is {}!'.format(next(idf), next(idf), next(idf), next(idf), next(pp))
print '{} is a {}, if {} works at {}, the utility is {}!'.format(next(idf), next(idf), next(idf), next(idf), next(pp))
print '{} is a {}, if {} works at {}, the utility is {}!'.format(next(idf), next(idf), next(idf), next(idf), next(pp))
print '{} is a {}, if {} works at {}, the utility is {}!'.format(next(idf), next(idf), next(idf), next(idf), next(pp))
print '{} is a {}, if {} works at {}, the utility is {}!'.format(next(idf), next(idf), next(idf), next(idf), next(pp))
print '{} is a {}, if {} works at {}, the utility is {}!'.format(next(idf), next(idf), next(idf), next(idf), next(pp))
print '{} is a {}, if {} works at {}, the utility is {}!'.format(next(idf), next(idf), next(idf), next(idf), next(pp))
print '{} is a {}, if {} works at {}, the utility is {}!'.format(next(idf), next(idf), next(idf), next(idf), next(pp))
print '{} is a {}, if {} works at {}, the utility is {}!'.format(next(idf), next(idf), next(idf), next(idf), next(pp))
print '{} is a {}, if {} works at {}, the utility is {}!'.format(next(idf), next(idf), next(idf), next(idf), next(pp))
print '{} is a {}, if {} works at {}, the utility is {}!'.format(next(idf), next(idf), next(idf), next(idf), next(pp))
print '{} is a {}, if {} works at {}, the utility is {}!'.format(next(idf), next(idf), next(idf), next(idf), next(pp))
print '{} is a {}, if {} works at {}, the utility is {}!'.format(next(idf), next(idf), next(idf), next(idf), next(pp))

# OUTPUT RESULT
# Amy is a Entrepreneur, if Amy works at Investment Bank, the utility is 82!
# Amy is a Entrepreneur, if Amy works at Startup, the utility is 164!
# Bob is a Slacker, if Bob works at Startup, the utility is -40!
# Bob is a Slacker, if Bob works at Investment Bank, the utility is -76!
# Christine is a Slacker, if Christine works at Big Software Firm, the utility is -34!
# Christine is a Slacker, if Christine works at Investment Bank, the utility is -76!
# Christine is a Slacker, if Christine works at Grad School, the utility is -13!
# David is a Money Grubber, if David works at Big Software Firm, the utility is 78!
# David is a Money Grubber, if David works at Big Software Firm, the utility is 78!
# David is a Money Grubber, if David works at Investment Bank, the utility is 110!
# Elizabeth is a Academic, if Elizabeth works at Grad School, the utility is 102!
# Elizabeth is a Academic, if Elizabeth works at Hedge Fund, the utility is 60!
# Elizabeth is a Academic, if Elizabeth works at Grad School, the utility is 102!
