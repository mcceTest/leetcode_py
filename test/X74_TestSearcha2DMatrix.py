import unittest

from X74_Searcha2DMatrix import Solution

class TestSum(unittest.TestCase):

    def test1(self):
        sol = Solution()
        matrix = [
        [1,   3,  5,  7],
        [10, 11, 16, 20],
        [23, 30, 34, 50]
        ]
        target = 3

        self.assertTrue(sol.searchMatrix(matrix, target))


    def test2(self):
        sol = Solution()
        matrix = [
        [1,   3,  5,  7],
        [10, 11, 16, 20],
        [23, 30, 34, 50]
        ]
        target = 13

        self.assertFalse(sol.searchMatrix(matrix, target))
    

       
if __name__ == "__main__":
    unittest.main()