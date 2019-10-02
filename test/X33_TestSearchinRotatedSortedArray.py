import unittest

from X33_SearchinRotatedSortedArray import Solution


class TestSum(unittest.TestCase):

    def test1(self):
        sol = Solution()
        nums = [4,5,6,7,0,1,2]
        target = 0

        self.assertEqual(sol.search(nums, target), 4)

    def test2(self):
        sol = Solution()
        nums = [4,5,6,7,0,1,2]
        target = 3

        self.assertEqual(sol.search(nums, target), -1)

    def test3(self):
        sol = Solution()
        nums = [3, 1]
        target = 1

        self.assertEqual(sol.search(nums, target), 1)

        
       
if __name__ == "__main__":
    unittest.main()