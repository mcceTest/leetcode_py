import unittest
from X119_PascalsTriangleII import Solution
class TestSum(unittest.TestCase):

    def test1(self):
        sol = Solution()
        rowIndex = 3
        self.assertListEqual(sol.getRow(rowIndex), [1,3,3,1])

    def test2(self):
        sol = Solution()
        rowIndex = 0
        self.assertListEqual(sol.getRow(rowIndex), [1])

    def test3(self):
        sol = Solution()
        rowIndex = 1
        self.assertListEqual(sol.getRow(rowIndex), [1, 1])

    def test4(self):
        sol = Solution()
        rowIndex = 2
        self.assertListEqual(sol.getRow(rowIndex), [1, 2, 1])


if __name__ == "__main__":
    unittest.main()