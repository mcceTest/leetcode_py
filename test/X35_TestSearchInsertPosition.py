import unittest

from X35_SearchInsertPosition import Solution


class TestSum(unittest.TestCase):

    def test1(self):
        sol = Solution()
        nums = [1,3,5,6]
        target = 5

        self.assertEqual(sol.searchInsert(nums, target), 2)

    def test2(self):
        sol = Solution()
        nums = [1,3,5,6]
        target = 2

        self.assertEqual(sol.searchInsert(nums, target), 1)

    def test3(self):
        sol = Solution()
        nums = [1,3,5,6]
        target = 7

        self.assertEqual(sol.searchInsert(nums, target), 4)

    def test4(self):
        sol = Solution()
        nums = [1,3,5,6]
        target = 0

        self.assertEqual(sol.searchInsert(nums, target), 0)
        
       
if __name__ == "__main__":
    unittest.main()