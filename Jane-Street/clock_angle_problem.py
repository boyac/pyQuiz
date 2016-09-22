# -*- coding: utf-8 -*-
# @Author: boyac
# @Date:   2016-09-19 18:09:38
# @Last Modified by:   boyac
# @Last Modified time: 2016-09-21 12:44:32

'''
Questions:
(1) What's the angle between the two arms of a clock when it is   at 2:30? 

(2) At a certain time between 3pm and 4pm, 
the hour and the minute hands are at equal angles from the 6 mark, 
what time will it be exactly?
'''

def clock_angle(hour, minute):
	# return abs(0.5 * (60 * hour - 11 * minute))
	return abs(30 * hour - 5.5 * minute)

def superimposed(hour):
	return 'Time = {}:{}'.format(hour, 5.45 * hour)



if __name__ == '__main__':
	print clock_angle(2, 30) # 105.0
	print clock_angle(3, 15) # 7.5
	print superimposed(3) # Time = 3:16.35
