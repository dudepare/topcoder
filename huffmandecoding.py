"""
SRM 308
https://community.topcoder.com/stat?c=problem_statement&pm=6477&rd=9988
"""
import unittest

class HuffmanDecoding:

	def decode(self, archive, dictionary):
		a_len = len(archive)
		d_len = len(dictionary)
		result = []
		start = 0

		for i in range(1, a_len+1, 1):
			search = archive[start:i]
			for j, val in enumerate(dictionary):
				if search == val:
					result.append(chr(ord('A') + j))
					if i != a_len:
						start = i
					break

		return "".join(result)

class TestHuffmanDecoding(unittest.TestCase):

	def setUp(self):
		self.obj = HuffmanDecoding()

	def callFn(self, archive, dictionary):
		return self.obj.decode(archive, dictionary)

	def tests(self):
		self.assertEqual("BDC", self.callFn("101101", ["00", "10", "01", "11"]))
		self.assertEqual("CBAC", self.callFn("10111010", ["0", "111", "10"]))
		self.assertEqual("BBBABBAABBABBAAABBA", self.callFn("0001001100100111001", ["1", "0"]))
		self.assertEqual("EGGFAC", self.callFn("111011011000100110", ["010", "00", "0110", "0111", "11", "100", "101"]))
		self.assertEqual("A", self.callFn("00000000000000000000000000000000000000000000000000", ["00000000000000000000000000000000000000000000000000", "11111111111111111111111111111111111111111111111111"]))

if __name__ == '__main__':
	unittest.main()
