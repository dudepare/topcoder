"""
SRM 437
https://community.topcoder.com/stat?c=problem_statement&pm=10233
"""
import unittest

class TheBeauty:

	def find(self, number):

		snumber = set(str(number))
		return len(snumber)

class TestTheBeauty(unittest.TestCase):

	def setUp(self):
		self.obj = TheBeauty()

	def callFn(self, number):
		return self.obj.find(number)

	def tests(self):
		self.assertEqual(2, self.callFn(10000))
		self.assertEqual(3, self.callFn(10020))
		self.assertEqual(1, self.callFn(1))

if __name__ == '__main__':
	unittest.main()
