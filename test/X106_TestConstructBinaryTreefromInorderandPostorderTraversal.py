import unittest
from X106_ConstructBinaryTreefromInorderandPostorderTraversal import Solution
from treeNode import TreeNode
class TestSum(unittest.TestCase):

    def test1(self):
        sol = Solution()
        inorder = [9,3,15,20,7]
        postorder = [9,15,7,20,3]
        node = sol.buildTree(inorder, postorder)

        self.assertTrue(TreeNode.isSameTree(node, TreeNode.constructFromLevelList([3, 9, 20, None, None, 15, 7])))       


if __name__ == "__main__":
    unittest.main()