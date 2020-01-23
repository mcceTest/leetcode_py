import unittest
from X134_GasStation import Solution

class TestSum(unittest.TestCase):

    def test1(self):
        sol = Solution()
        gas  = [1,2,3,4,5]
        cost = [3,4,5,1,2]
        self.assertEqual(sol.canCompleteCircuit(gas, cost), 3)


    def test2(self):
        sol = Solution()
        gas  = [2,3,4]
        cost = [3,4,3]
        self.assertEqual(sol.canCompleteCircuit(gas, cost), -1)


if __name__ == "__main__":
    unittest.main()