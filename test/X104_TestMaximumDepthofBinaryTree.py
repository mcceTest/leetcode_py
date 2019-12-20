import unittest
from X104_MaximumDepthofBinaryTree import Solution
from treeNode import TreeNode
class TestSum(unittest.TestCase):

    def test1(self):
        sol = Solution()
        root = TreeNode.constructFromLevelList([3,9,20,None,None,15,7])
        self.assertEqual(sol.maxDepth(root), 3)

    def test2(self):
        sol = Solution()
        self.assertEqual(sol.maxDepth(None), 0)
                           
if __name__ == "__main__":
    unittest.main()