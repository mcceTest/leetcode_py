import unittest

from X41_FirstMissingPositive import Solution


class TestSum(unittest.TestCase):

    def test1(self):
        sol = Solution()
        nums = [1,2,0]

        self.assertEqual(sol.firstMissingPositive(nums), 3)

    def test2(self):
        sol = Solution()
        nums = [3,4,-1,1]

        self.assertEqual(sol.firstMissingPositive(nums), 2)

    def test3(self):
        sol = Solution()
        nums = [7,8,9,11,12]

        self.assertEqual(sol.firstMissingPositive(nums), 1)
        
       
if __name__ == "__main__":
    unittest.main()