"""
SRM 288
https://community.topcoder.com/stat?c=problem_statement&pm=6036
"""
import unittest

class AccountBalance:

    def processTransactions(self, startingBalance, transactions):
        
        if not transactions:
            return startingBalance

        for t in transactions:
            item = t.split()
            operation, amount = item[0], int(item[1])
            if operation is 'C':
                startingBalance += amount
            else:
                startingBalance -= amount

        return startingBalance            


class TestAccountBalance(unittest.TestCase):

    def setUp(self):
        self.obj = AccountBalance()

    def callFn(self, startingBalance, transactions):
        return self.obj.processTransactions(startingBalance, transactions)

    def tests(self):
        self.assertEqual(250, self.callFn(100, ["C 1000", "D 500", "D 350"] ))
        self.assertEqual(100, self.callFn(100, [] ))
        self.assertEqual(-10, self.callFn(100, ["D 50", "D 20", "D 40"]))
        self.assertEqual(10580, self.callFn(53874, ["D 1234", "C 987", "D 2345", "C 654", "D 6789", "D 34567"]))

if __name__ == '__main__':
    unittest.main()
