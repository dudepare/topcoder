import unittest

# top coder problem set
# https://community.topcoder.com/tc?module=HSProblemStatement&pm=7558&rd=10721

class AdvertisingAgency():

	def numberOfRejections(self, requests):
		rejected = 0

		for i in range(len(requests)):
			if requests[i] != -1:
				for j in range(i+1, len(requests)):
					if requests[i] == requests[j]:
						requests[j] = -1
						rejected += 1
		return rejected

class TestAdvertisingAgency(unittest.TestCase):

	def setUp(self):
		self.advert = AdvertisingAgency()

	def testNoRejects(self):
		self.assertEqual( 0, self.advert.numberOfRejections([1,2,3]))

	def testOneReject(self):
		self.assertEqual( 1, self.advert.numberOfRejections([1,2,3,1]))

	def testLotsOfReject(self):
		self.assertEqual( 16,
		                 self.advert.numberOfRejections([1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]))

if __name__ == '__main__':
	unittest.main()
