"""
SRM 560
https://community.topcoder.com/stat?c=problem_statement&pm=12297&rd=15182
"""
import unittest

class TypingDistance:

	def minDistance(self, keyboard, word):
		
		distance = 0
		x = 0
		y = 0

		for i in range(len(word)-1):
			x = 0
			y = 0
			if i+1 < len(word):
				while keyboard[x] != word[i]:
					x += 1
				while keyboard[y] != word[i+1]:
					y += 1
				
				if x > y:
					distance += (x-y)
				else:
					distance += (y-x)
				
		return distance 

class TestTypingDistance(unittest.TestCase):

	def setUp(self):
		self.obj = TypingDistance()

	def callFn(self, keyboard, word):
		return self.obj.minDistance(keyboard, word)

	def tests(self):
		self.assertEqual(8, self.callFn("qwertyuiop", "potter"))
		self.assertEqual(39, self.callFn("kwadrutove", "rowerowe"))
		self.assertEqual(322, self.callFn("qwertyuiopasdfghjklzxcvbnm",
		                                "topcodersingleroundmatchgoodluckhavefun"))
		self.assertEqual(0, self.callFn("d", "dddddddddddddddddddddddddddddddddddddddddddddddddd"))
		self.assertEqual(13, self.callFn("co", "coccooccocoococoocccoo"))

if __name__ == '__main__':
	unittest.main()
