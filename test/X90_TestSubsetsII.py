import unittest
from X90_SubsetsII import Solution

class TestSum(unittest.TestCase):

    def test1(self):
        sol = Solution()
        nums = [1,2,2]

        self.assertListEqual(sorted(sol.subsetsWithDup(nums)), sorted([
                                                                        [2],
                                                                        [1],
                                                                        [1,2,2],
                                                                        [2,2],
                                                                        [1,2],
                                                                        []
                                                                        ]))
    def test2(self):
        sol = Solution()
        nums = [1,2]

        self.assertListEqual(sorted(sol.subsetsWithDup(nums)), sorted([
                                                                        [2],
                                                                        [1],
                                                                        [1,2],
                                                                        []
                                                                        ]))

    def test3(self):
        sol = Solution()
        nums = [1,2,2,1]

        self.assertListEqual(sorted(sol.subsetsWithDup(nums)), sorted([
                                                                        [2],
                                                                        [1],
                                                                        [1,2],
                                                                        [],
                                                                        [1,1,2],
                                                                        [1,2,2],
                                                                        [1,1,2,2],
                                                                        [1,1],
                                                                        [2,2]
                                                                        ]))                                                                    

if __name__ == "__main__":
    unittest.main()