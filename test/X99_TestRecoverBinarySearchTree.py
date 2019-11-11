import unittest
from X99_RecoverBinarySearchTree import Solution
from treeNode import TreeNode
class TestSum(unittest.TestCase):

    def test1(self):
        sol = Solution()
        root = TreeNode.constructFromLevelList([1,3,None, None,2])
        sol.recoverTree(root)
        self.assertListEqual(TreeNode.toList(root), [3,1,None, None, 2])
        
    def test2(self):
        sol = Solution()
        root = TreeNode.constructFromLevelList([3,1,4,None,None,2])
        sol.recoverTree(root)
        self.assertListEqual(TreeNode.toList(root), [2,1,4,None,None,3])
                           
if __name__ == "__main__":
    unittest.main()