import unittest
from X123_BestTimetoBuyandSellStockIII import Solution
class TestSum(unittest.TestCase):

    def test1(self):
        sol = Solution()
        prices = [3,3,5,0,0,3,1,4]
        self.assertEqual(sol.maxProfit(prices), 6)


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