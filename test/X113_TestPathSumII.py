import unittest
from X113_PathSumII import Solution
from treeNode import TreeNode
class TestSum(unittest.TestCase):

    def test1(self):
        sol = Solution()
        root = TreeNode.constructFromLevelList([5,4,8,11,None, 13, 4, 7, 2, None,None,5,1])
        self.assertListEqual(sorted(sol.pathSum(root, 22)), sorted([[5, 4, 11, 2], [5, 8, 4, 5]]))


if __name__ == "__main__":
    unittest.main()