"""
SRM 573
https://community.topcoder.com/tc?module=ProblemDetail&rd=15493&pm=12469
"""
import unittest

class SkiResortEasy:

	def minCost(self, arr_list):

		n = len(arr_list)
		total = 0

		for i in range(n-1):
			if (arr_list[i+1] > arr_list[i]):
				total += (arr_list[i+1] - arr_list[i])
				arr_list[i+1] = arr_list[i]

		return total

class TestSkiResortEasy(unittest.TestCase):

	def setUp(self):
		self.testObj = SkiResortEasy()

	def callFn(self, arr_list):
		return self.testObj.minCost(arr_list)

	def tests(self):
		self.assertEqual(0, self.callFn([30, 20, 20, 10]))
		self.assertEqual(2, self.callFn([5, 7, 3]))
		self.assertEqual(6, self.callFn([6, 8, 5, 4, 7, 4, 2, 3, 1]))
		self.assertEqual(2284, self.callFn([749, 560, 921, 166, 757, 818, 228, 584, 366, 88]))
		self.assertEqual(6393, self.callFn([712, 745, 230, 200, 648, 440, 115, 913, 627, 621, 186, 222, 741, 954, 581, 193, 266, 320, 798, 745]))

if __name__ == '__main__':
	unittest.main()
