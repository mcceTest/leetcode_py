import unittest
from X149_MaxPointsonaLine import Solution
from listNode import ListNode


class TestSum(unittest.TestCase):

    def test1(self):
        sol = Solution()
        points = [[1,1],[2,2],[3,3]]
        self.assertEqual(sol.maxPoints(points), 3)


    def test2(self):
        sol = Solution()
        points = [[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]
        self.assertEqual(sol.maxPoints(points), 4)

if __name__ == "__main__":
    unittest.main()