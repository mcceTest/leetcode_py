import unittest
from X188_BestTimetoBuyandSellStockIV import Solution


class TestSum(unittest.TestCase):

    def test1(self):
        sol = Solution()
        prices = [2,4,1]
        k = 2
        self.assertEqual(sol.maxProfit(k, prices), 2)

    def test2(self):
        sol = Solution()
        prices = [3,2,6,5,0,3]
        k = 2
        self.assertEqual(sol.maxProfit(k, prices), 7)

    def test3(self):
        sol = Solution()
        prices = [2,1]
        k = 1
        self.assertEqual(sol.maxProfit(k, prices), 0)

    def test4(self):
        sol = Solution()
        prices = [3,3,5,0,0,3,1,4]
        k = 2
        self.assertEqual(sol.maxProfit(k, prices), 6)


if __name__ == "__main__":
    unittest.main()