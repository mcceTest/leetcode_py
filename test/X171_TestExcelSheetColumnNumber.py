import unittest
from X171_ExcelSheetColumnNumber import Solution


class TestSum(unittest.TestCase):

    def test1(self):
        sol = Solution()
        s = 'A'
        self.assertEqual(sol.titleToNumber(s), 1)


    def test2(self):
        sol = Solution()
        s = 'AB'
        self.assertEqual(sol.titleToNumber(s), 28)


    def test3(self):
        sol = Solution()
        s = 'ZY'
        self.assertEqual(sol.titleToNumber(s), 701)


    


if __name__ == "__main__":
    unittest.main()