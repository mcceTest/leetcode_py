import unittest

from X31_NextPermutation import Solution


class TestSum(unittest.TestCase):

    def test1(self):
        sol = Solution()

        nums = [1, 2, 3]
        sol.nextPermutation(nums)

        self.assertListEqual(nums, [1, 3, 2])


    def test2(self):
        sol = Solution()

        nums = [3, 2, 1]
        sol.nextPermutation(nums)

        self.assertListEqual(nums, [1, 2, 3])


    def test3(self):
        sol = Solution()

        nums = [1, 1, 5]
        sol.nextPermutation(nums)

        self.assertListEqual(nums, [1, 5, 1])

    def test4(self):
        sol = Solution()

        nums = [1, 3, 2]
        sol.nextPermutation(nums)

        self.assertListEqual(nums, [2, 1, 3])




   
        
       
if __name__ == "__main__":
    unittest.main()