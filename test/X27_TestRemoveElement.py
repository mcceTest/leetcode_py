import unittest

from X27_RemoveElement import Solution


class TestSum(unittest.TestCase):

    def test1(self):
        sol = Solution()

        nums = [3,2,2,3]
        length = sol.removeElement(nums, 3)

        self.assertEqual(length, 2)
        self.assertListEqual(nums[:length], [2, 2])


    def test2(self):
        sol = Solution()

        nums = [0,1,2,2,3,0,4,2]
        length = sol.removeElement(nums, 2)

        self.assertEqual(length, 5)
        self.assertListEqual(nums[:length], [0, 1, 3, 0, 4])



        
        
       
if __name__ == "__main__":
    unittest.main()