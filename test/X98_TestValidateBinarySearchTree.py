import unittest
from X98_ValidateBinarySearchTree import Solution
from treeNode import TreeNode
class TestSum(unittest.TestCase):

    def test1(self):
        sol = Solution()
        root = TreeNode.constructFromLevelList([2,1,3])
        self.assertTrue(sol.isValidBST(root))

    def test2(self):
        sol = Solution()
        root = TreeNode.constructFromLevelList([5,1,4,None,None,3,6])
        self.assertFalse(sol.isValidBST(root))
        
                           
if __name__ == "__main__":
    unittest.main()