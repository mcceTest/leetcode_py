import unittest
from X94_BinaryTreeInorderTraversal import Solution
from treeNode import TreeNode

class TestSum(unittest.TestCase):

    def test1(self):
        sol = Solution()
        root = TreeNode(1)
        root.right = TreeNode(2)
        root.right.left = TreeNode(3)

        self.assertListEqual(sol.inorderTraversal(root), [1,3,2])
        
    def test2(self):
        sol = Solution()
        root = TreeNode(1)
        
        self.assertListEqual(sol.inorderTraversal(root), [1])
                           
if __name__ == "__main__":
    unittest.main()