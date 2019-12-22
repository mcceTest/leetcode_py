import unittest
from X107_BinaryTreeLevelOrderTraversalII import Solution
from treeNode import TreeNode
class TestSum(unittest.TestCase):

    def test1(self):
        sol = Solution()
        root = TreeNode.constructFromLevelList([3,9,20,None,None,15,7])
        self.assertListEqual(sol.levelOrderBottom(root), [
                                                            [15,7],
                                                            [9,20],
                                                            [3]
                                                            ])


if __name__ == "__main__":
    unittest.main()