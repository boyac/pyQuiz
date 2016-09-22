__author__ = 'Boya Chiou'

import itertools

class NameSpot:
	""" 
	Return suspicious name of a transaction spending more than $3000;
	and a transaction for which the next transaction for the same person 
	differs in location, and is less than an hour later.
	"""
	def __init__(self, result1=[], result2=[]):
		self.result1 = result1
		self.result2 = result2

	def lines(self):
		with open('p_input.txt') as f:
			for line in f:
				yield line.strip().split('|')		

	def parse(self, *file):
		"""
		Mission 1: Spot a transaction spending more than $3000
		"""
		for line in self.lines():
			if int(line[1]) > 3000: # A transaction spending more than $3000
				self.result1.append(line[0])
		return 'A transaction spending more than $3000: {}'.format(self.result1)

	def parse_2(self): 
		"""
		Mission 2: Spot a transaction for which the next transaction for 
		the same person differs in location, and is less than an hour later
		"""
		for line1, line2 in itertools.combinations(self.lines(), 2):
			if line1[0] == line2[0]:
				if line1[2] != line2[2]:
					if int(line1[3]) - int(line2[3]) < 60:
						self.result2.append(line1[0])
		return 'The same person differs in location, and is less than an hour: {}'.format(set(self.result2))
	
	def merge_list(self):
		return 'All Suspicious Name List: {}'.format(set(self.result1 + self.result2))


spot = NameSpot()
it = spot.lines()
print spot.parse(*it)       # A transaction spending more than $3000: ['Krasi', 'Matt', 'Jay']
print spot.parse_2(*it)     # The same person differs in location, and is less than an hour: set(['Shilpa', 'Krasi'])
print spot.merge_list(*it)  # All Suspicious Name List: set(['Matt', 'Shilpa', 'Krasi', 'Jay'])
