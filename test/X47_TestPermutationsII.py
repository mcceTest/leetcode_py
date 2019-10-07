import unittest

from X47_PermutationsII import Solution


class TestSum(unittest.TestCase):

    def test1(self):
        sol = Solution()
        nums = [1,1,2]

        self.assertListEqual(sorted(sol.permuteUnique(nums)), sorted([
                                                                    [1,1,2],
                                                                    [1,2,1],
                                                                    [2,1,1]
                                                                    ]))


    
       
if __name__ == "__main__":
    unittest.main()