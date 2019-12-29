import unittest
from X121_BestTimetoBuyandSellStock import Solution
class TestSum(unittest.TestCase):

    def test1(self):
        sol = Solution()
        prices = [7,1,5,3,6,4]
        self.assertEqual(sol.maxProfit(prices), 5)

    def test2(self):
        sol = Solution()
        prices = [7,6,4,3,1]
        self.assertEqual(sol.maxProfit(prices), 0)

if __name__ == "__main__":
    unittest.main()