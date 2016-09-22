"""
Question 1.57: You have an array that contains 99 distinct integers from the set {1, 2, 3, . . . , 100}. 
How would you write a program to figure out which integer is missing?
"""
lst1 = range(1,101)
lst2 = range(1,101)
lst2.remove(13)
lst2.remove(17)


def missing(lst1, lst2):
	return set(lst1).difference(lst2)

print missing(lst1, lst2)
