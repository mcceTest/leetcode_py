import unittest
from X4_MedianofTwoSortedArrays import Solution


class TestSum(unittest.TestCase):

    def test1(self):
        sol = Solution()

        self.assertEqual(sol.findMedianSortedArrays([1, 3], [2]), 2)

        self.assertEqual(sol.findMedianSortedArrays([1, 2], [3, 4]), 2.5)

        self.assertEqual(sol.findMedianSortedArrays([3, 4], [1, 2]), 2.5)

        self.assertEqual(sol.findMedianSortedArrays([1], [3]), 2)

        self.assertEqual(sol.findMedianSortedArrays([1], []), 1)

        self.assertEqual(sol.findMedianSortedArrays([], []), 0)
        
        self.assertEqual(sol.findMedianSortedArrays([], [2]), 2)

        self.assertEqual(sol.findMedianSortedArrays([1], [3, 4]), 3)

        self.assertEqual(sol.findMedianSortedArrays([4], [1, 2, 3, 5]), 3)

        self.assertEqual(sol.findMedianSortedArrays([5, 6], [1, 2, 3, 4, 4, 6]), 4)

        self.assertEqual(sol.findMedianSortedArrays([1, 2, 3], [3, 4, 5]), 3)

        self.assertEqual(sol.findMedianSortedArrays([3, 4, 5], [1, 2, 3]), 3)

        self.assertEqual(sol.findMedianSortedArrays([4], [1, 2, 3]), 2.5)

if __name__ == "__main__":
    unittest.main()