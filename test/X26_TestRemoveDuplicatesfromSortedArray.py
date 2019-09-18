import unittest

from X26_RemoveDuplicatesfromSortedArray import Solution


class TestSum(unittest.TestCase):

    def test1(self):
        sol = Solution()

        nums = [1,1,2]

        length = sol.removeDuplicates(nums)
        self.assertEqual(length, 2)
        self.assertListEqual(nums[:length], [1, 2])


    def test2(self):
        sol = Solution()

        nums = [0,0,1,1,1,2,2,3,3,4]

        length = sol.removeDuplicates(nums)
        self.assertEqual(length, 5)
        self.assertListEqual(nums[:length], [0, 1, 2, 3, 4])

        
        
       
if __name__ == "__main__":
    unittest.main()