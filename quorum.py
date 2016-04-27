"""
SRM 687
https://community.topcoder.com/tc?module=ProblemDetail&rd=16708&pm=14219
"""
import unittest

class Quorum:

	def count(self, arr, n):
		arr.sort()
		i = 0
		ans = 0
		while i < n:
			ans += arr[i]
			i += 1
		return ans

class  TestQuorum(unittest.TestCase):

	def setUp(self):
		self.obj = Quorum()

	def callFn(self, arr, n):
		return self.obj.count(arr, n)

	def tests(self):
		self.assertEqual(2, self.callFn([5,2,3], 1))
		self.assertEqual(5, self.callFn([1, 1, 1, 1, 1], 5))
		self.assertEqual(49, self.callFn([50, 2, 9, 49, 38], 3))
		self.assertEqual(105, self.callFn([20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1], 14))

if __name__ == '__main__':
	unittest.main()