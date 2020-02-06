import unittest
from X145_BinaryTreePostorderTraversal import Solution
from treeNode import TreeNode

class TestSum(unittest.TestCase):

    def test1(self):
        sol = Solution()
        root = TreeNode.constructFromLevelList([1, None, 2, 3])
        self.assertListEqual(sol.postorderTraversal(root), [3,2,1])

    def test2(self):
        sol = Solution()
        root = TreeNode.constructFromLevelList([1, None, 2])
        self.assertListEqual(sol.postorderTraversal(root), [2,1])

    def test3(self):
        sol = Solution()
        root = TreeNode.constructFromLevelList([1, None, 2, None, 3])
        self.assertListEqual(sol.postorderTraversal(root), [3,2,1])

if __name__ == "__main__":
    unittest.main()