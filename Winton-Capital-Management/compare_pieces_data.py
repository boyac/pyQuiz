# -*- coding: utf-8 -*-
# @Author: boyac
# @Date:   2016-07-15 02:58:19
# @Last Modified by:   boyac
# @Last Modified time: 2016-07-15 03:14:11

import itertools
# compare and check if two pieces of data are the same

def compare(data1, data2):
	if data1 == data2:
		return 'They are the same!'
	else:
		return 'Not the same!'

def data(data_list):
	# return the combinations of data you'd like to compare
	return list(itertools.combinations(data_list, 2))


if __name__ == '__main__':
	agg_a = [110,110,111,111,111]
	agg_b = [110,110,111,111,111]
	spy = [110,110,111,111,112]
	data_list = [agg_a,agg_b,spy]
	print compare(agg_a,agg_b)
	print compare(agg_a, spy)
	print '---used combinations---'
	d = data(data_list)
	for i,j in d:
		print compare(i,j)
		
'''
result:

They are the same!
Not the same!
---used combinations---
They are the same!
Not the same!
Not the same!
[Finished in 0.0s]
'''
