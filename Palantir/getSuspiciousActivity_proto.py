__author__ = 'Boya Chiou'
#file = open('p_input.txt')

def lines():
	with open('p_input.txt') as f:
		for line in f:
			yield line.strip().split('|')		
			
def parse(*file):
	"""
	Mission 1: Spot a transaction spending more than $3000
	"""
	result = []
	for line in lines():
		if int(line[1]) > 3000: # A transaction spending more than $3000
			result.append(line[0])
	return result

def parse_2(*file): 
	"""
	Mission 2: Spot a transaction for which the next transaction for 
	the same person differs in location, and is less than an hour later
	"""
	result_2 = []
	rows_generator = lines()
	next_row = next(rows_generator, None)
	for line in lines(): # This result_2 failed, as it seems only takes the 1st row to compare the rest, instead of moving simultaneously
		if line[0] == next_row[0]:
			if line[2] != next_row[2]:
				if int(line[3]) - int(next_row[3]) < 60:
					result_2.append(next_row[0])
	return result_2 

it = lines()
print parse(*it)
print parse_2(*it)
