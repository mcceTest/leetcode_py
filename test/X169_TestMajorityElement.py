import unittest
from X169_MajorityElement import Solution


class TestSum(unittest.TestCase):

    def test1(self):
        sol = Solution()
        nums = [3,2,3]
        self.assertEqual(sol.majorityElement(nums), 3)

    def test2(self):
        sol = Solution()
        nums = [2,2,1,1,1,2,2]
        self.assertEqual(sol.majorityElement(nums), 2)


    def test3(self):
        sol = Solution()
        nums = [6,5,5]
        self.assertEqual(sol.majorityElement(nums), 5)


    


if __name__ == "__main__":
    unittest.main()