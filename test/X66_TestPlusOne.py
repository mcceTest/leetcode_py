import unittest

from X66_PlusOne import Solution

class TestSum(unittest.TestCase):

    def test1(self):
        sol = Solution()
        digits = [1,2,3]
        self.assertListEqual(sol.plusOne(digits), [1,2,4])

    def test2(self):
        sol = Solution()
        digits = [4,3,2,1]
        self.assertListEqual(sol.plusOne(digits), [4,3,2,2])

    def test3(self):
        sol = Solution()
        digits = [9]
        self.assertListEqual(sol.plusOne(digits), [1, 0])

    

       
if __name__ == "__main__":
    unittest.main()