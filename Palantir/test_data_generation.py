__author__ = 'Boya Chiou'

import random
import time 
#import memory_profiler

def people_list(num_people):
	"""
	Generating test sample by randomly assign the values to designated index
	Just paste the generated data into our p_input_test.txt
	Feel free to modify the code if you can incorporate the randomization generator in the main script (getSuspiciousActivity.py)
	Besides, I'd suggest to see if there's <names> or <location> (ref: https://pypi.python.org/pypi/fake-factory) 
	module to generate more name and location. Because basically after 1,000,000 rows sampling,
	you'd see every name listed below appear at least once.
	"""
	
	result = []
	names = ['John', 'Corey', 'Adam', 'Steve', 'Rick', 'Thomas', 'Alex', 'William', 'Eric', 'Shawn', 'Lindsey', 'Shilpa', 'Tom', 'Krasi', 'Matt', 'Max', 'Jay']
	amount = range(25, 5000, 10)
	location = ['California', 'Michigan', 'Georgia', 'Virginia', 'London', 'Rome', 'Tokyo', 'Singapore', 'New York', 'San Francisco', 'Florida', 'Palo Alto', 'Boston', 'Paris', 'Hong Kong', 'Beijing']
	time = range(0,2401)
	
	for i in range(num_people):
		result.append('{}|{}|{}|{}'.format(random.choice(names), random.choice(amount), random.choice(location), random.choice(time)))
	return result


for i in people_list(1000000):
	print i
