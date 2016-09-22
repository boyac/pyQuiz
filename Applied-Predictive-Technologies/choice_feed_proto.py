import itertools

class Data():
  """
  Merge two generators for mission 1 to get the product of utility of personality*offers
  """
	def __init__(self):
		pass
		
	def lines(self):
		with open('people_proto.txt') as file:
			for line in file:
				yield line.strip().split(' | ')

	def data_people(self):
		with open('people_proto.txt') as file1:
			for line in file1:
				yield line.strip().split(' | ')
	
	def data_offers(self):
		with open('offers_proto.txt') as file2:
			for line in file2:
				yield line.strip().split(' | ')

	def data_merge(self, *file):
		"""
		merge data by maching key == name:
		"""
		for line1 in self.data_people():
			for line2 in self.data_offers():
				if line1[0] == line2[0]:
					yield list(itertools.chain(line1, line2))
	


m = Data()
it = m.lines()
pp = m.data_people()
oo = m.data_offers()
merge = m.data_merge()

print next(merge)	# ['Amy', 'Slacker', 'Amy', 'Hofferman Smith-Daniels', 'Investment Bank', 'San Francisco']
print next(merge)	# ['Amy', 'Slacker', 'Amy', 'Bigup-Side', 'Startup', 'Washington, DC']
print next(merge)	# ['Bob', 'Slacker', 'Bob', 'Irreverent Technologies', 'Startup', 'NYC']
print next(merge)	# ['Bob', 'Slacker', 'Bob', 'Hofferman Smith-Daniels', 'Investment Bank', 'San Francisco']
print next(merge)	# ['Christine', 'Slacker', 'Christine', 'InnoTech', 'Big Software Firm', 'Washington, DC']
