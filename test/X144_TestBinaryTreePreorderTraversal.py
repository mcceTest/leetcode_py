import unittest
from X144_BinaryTreePreorderTraversal import Solution
from treeNode import TreeNode

class TestSum(unittest.TestCase):

    def test1(self):
        sol = Solution()
        root = TreeNode.constructFromLevelList([1, None, 2, 3])
        self.assertListEqual(sol.preorderTraversal(root), [1,2,3])

    def test2(self):
        sol = Solution()
        root = TreeNode.constructFromLevelList([1, None, 2])
        self.assertListEqual(sol.preorderTraversal(root), [1,2])

    def test3(self):
        sol = Solution()
        root = TreeNode.constructFromLevelList([1, None, 2, None, 3])
        self.assertListEqual(sol.preorderTraversal(root), [1,2,3])

if __name__ == "__main__":
    unittest.main()