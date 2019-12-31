import unittest
from X124_BinaryTreeMaximumPathSum import Solution
from treeNode import TreeNode
class TestSum(unittest.TestCase):

    def test1(self):
        sol = Solution()
        root = TreeNode.constructFromLevelList([1,2,3])
        self.assertEqual(sol.maxPathSum(root), 6)


    def test2(self):
        sol = Solution()
        root = TreeNode.constructFromLevelList([-10,9,20,None,None,15,7])
        self.assertEqual(sol.maxPathSum(root), 42)

    def test3(self):
        sol = Solution()
        root = TreeNode.constructFromLevelList([-3])
        self.assertEqual(sol.maxPathSum(root), -3)


    def test4(self):
        sol = Solution()
        root = TreeNode.constructFromLevelList([1, -2, 3])
        self.assertEqual(sol.maxPathSum(root), 4)

if __name__ == "__main__":
    unittest.main()