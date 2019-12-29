import unittest
from X122_BestTimetoBuyandSellStockII import Solution
class TestSum(unittest.TestCase):

    def test1(self):
        sol = Solution()
        prices = [7,1,5,3,6,4]
        self.assertEqual(sol.maxProfit(prices), 7)

    def test2(self):
        sol = Solution()
        prices = [1,2,3,4,5]
        self.assertEqual(sol.maxProfit(prices), 4)

    def test3(self):
        sol = Solution()
        prices = [7,6,4,3,1]
        self.assertEqual(sol.maxProfit(prices), 0)

if __name__ == "__main__":
    unittest.main()