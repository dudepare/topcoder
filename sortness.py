# SRM 330
# https://community.topcoder.com/stat?c=problem_statement&pm=7263&rd=10010
# basically this assumes the sortness is in ascending order
import unittest

class Sortness:

	def getSortness(self, arr_list):

		size = len(arr_list)
		total = 0

		for i, ival in enumerate(arr_list):
			for j, jval in enumerate(arr_list):
				if (i < j and ival > jval or i >  j and ival < jval):
					total += 1
		return total/size 

class TestSortness(unittest.TestCase):

	def setUp(self):
		self.testObj = Sortness()

	def callFn(self, arr_list):
		return self.testObj.getSortness(arr_list)

	def tests(self):
		self.assertEqual( 0.0, self.callFn([1,2,3]))
		self.assertEqual( 1.25, self.callFn([3,2,1,4,6,7,5,8]))
		self.assertEqual( 4.0, self.callFn([5,4,3,2,1]))
		self.assertEqual( 5.166666666666667,
		                 self.callFn([1,5,8,7,9,6,10,12,11,3,4,2]))
		

if __name__ == '__main__':
	unittest.main()