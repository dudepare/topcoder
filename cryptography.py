"""
SRM 480
https://community.topcoder.com/stat?c=problem_statement&pm=10814&rd=14159
"""
import unittest

class Cryptography:

    def encrypt(self, items):
        
        result = 0
        product = 1
        for i in range(len(items)):
            items[i] += 1
            product = 1
            for j in items:
                product *= j
            if result < product:
                result = product
            items[i] -= 1
        return result

class TestCryptography(unittest.TestCase):

    def setUp(self):
        self.obj = Cryptography()

    def callFn(self, items):
        return self.obj.encrypt(items)

    def tests(self):
        self.assertEqual(12, self.callFn([1,2,3]))
        self.assertEqual(36, self.callFn([1,3,2,1,1,3]))
        self.assertEqual(986074810223904000, self.callFn([1000,999,998,997,996,995]))
        self.assertEqual(2, self.callFn([1,1,1,1]))

if __name__ == '__main__':
    unittest.main()
