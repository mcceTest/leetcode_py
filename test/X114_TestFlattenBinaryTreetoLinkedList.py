import unittest
from X114_FlattenBinaryTreetoLinkedList import Solution
from treeNode import TreeNode
class TestSum(unittest.TestCase):

    def test1(self):
        sol = Solution()
        root = TreeNode.constructFromLevelList([1, 2, 5, 3, 4, None, 6])
        root = sol.flatten(root)

        self.assertTrue(TreeNode.isSameTree(root, TreeNode.constructFromLevelList([1, None, 2, None, 3, None, 4, None, 5, None, 6])))


    def test2(self):
        sol = Solution()
        root = TreeNode.constructFromLevelList([1])
        root = sol.flatten(root)

        self.assertTrue(TreeNode.isSameTree(root, TreeNode.constructFromLevelList([1])))


    def test3(self):
        sol = Solution()
        root = TreeNode.constructFromLevelList([1, None, 2])
        root = sol.flatten(root)

        self.assertTrue(TreeNode.isSameTree(root, TreeNode.constructFromLevelList([1, None, 2])))


    def test4(self):
        sol = Solution()
        root = TreeNode.constructFromLevelList([1, 2, None])
        root = sol.flatten(root)

        self.assertTrue(TreeNode.isSameTree(root, TreeNode.constructFromLevelList([1, None, 2])))


if __name__ == "__main__":
    unittest.main()