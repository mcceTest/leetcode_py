import unittest
from X102_BinaryTreeLevelOrderTraversal import Solution
from treeNode import TreeNode
class TestSum(unittest.TestCase):

    def test1(self):
        sol = Solution()
        root = TreeNode.constructFromLevelList([3,9,20,None,None,15,7])
        self.assertListEqual(sol.levelOrder(root), [
                                                    [3],
                                                    [9,20],
                                                    [15,7]
                                                    ])
                           
if __name__ == "__main__":
    unittest.main()