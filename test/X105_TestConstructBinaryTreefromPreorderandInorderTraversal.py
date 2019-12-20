import unittest
from X105_ConstructBinaryTreefromPreorderandInorderTraversal import Solution
from treeNode import TreeNode
class TestSum(unittest.TestCase):

    def test1(self):
        sol = Solution()
        preorder = [3,9,20,15,7]
        inorder = [9,3,15,20,7]
        node = sol.buildTree(preorder, inorder)

        self.assertTrue(TreeNode.isSameTree(node, TreeNode.constructFromLevelList([3, 9, 20, None, None, 15, 7])))       


if __name__ == "__main__":
    unittest.main()