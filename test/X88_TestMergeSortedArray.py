import unittest
from X88_MergeSortedArray import Solution

class TestSum(unittest.TestCase):

    def test1(self):
        sol = Solution()
        nums1 = [1,2,3,0,0,0]
        m = 3
        nums2 = [2,5,6]
        n = 3
        
        sol.merge(nums1, n, nums2, m)

        self.assertListEqual(nums1, [1,2,2,3,5,6])


if __name__ == "__main__":
    unittest.main()