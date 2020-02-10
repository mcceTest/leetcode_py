import unittest
from X168_ExcelSheetColumnTitle import Solution


class TestSum(unittest.TestCase):

    def test1(self):
        sol = Solution()
        n = 1
        self.assertEqual(sol.convertToTitle(n), 'A')

    def test2(self):
        sol = Solution()
        n = 28
        self.assertEqual(sol.convertToTitle(n), 'AB')


    def test3(self):
        sol = Solution()
        n = 701
        self.assertEqual(sol.convertToTitle(n), 'ZY')


    def test4(self):
        sol = Solution()
        n = 26
        self.assertEqual(sol.convertToTitle(n), 'Z')


if __name__ == "__main__":
    unittest.main()