import unittest
from X112_PathSum import Solution
from treeNode import TreeNode
class TestSum(unittest.TestCase):

    def test1(self):
        sol = Solution()
        root = TreeNode.constructFromLevelList([5,4,8,11,None, 13, 4, 7, 2, None,None,None,1])
        self.assertTrue(sol.hasPathSum(root, 22))


if __name__ == "__main__":
    unittest.main()