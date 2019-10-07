import unittest

from X46_Permutations import Solution


class TestSum(unittest.TestCase):

    def test1(self):
        sol = Solution()
        nums = [1,2,3]

        self.assertListEqual(sorted(sol.permute(nums)), sorted([
                                                                [1,2,3],
                                                                [1,3,2],
                                                                [2,1,3],
                                                                [2,3,1],
                                                                [3,1,2],
                                                                [3,2,1]
                                                                ]))


    
       
if __name__ == "__main__":
    unittest.main()