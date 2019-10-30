import unittest

from X85_MaximalRectangle import Solution

class TestSum(unittest.TestCase):

    def test1(self):
        sol = Solution()
        matrix = [
                  ["1","0","1","0","0"],
                  ["1","0","1","1","1"],
                  ["1","1","1","1","1"],
                  ["1","0","0","1","0"]
                ]

        self.assertEqual(sol.maximalRectangle(matrix), 6)


if __name__ == "__main__":
    unittest.main()