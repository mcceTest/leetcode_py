import unittest
from X101_SymmetricTree import Solution
from treeNode import TreeNode
class TestSum(unittest.TestCase):

    def test1(self):
        sol = Solution()
        root = TreeNode.constructFromLevelList([1,2,2,3,4,4,3])
        self.assertTrue(sol.isSymmetric(root))
        
    def test2(self):
        sol = Solution()
        root = TreeNode.constructFromLevelList([1,2,2,None,3,None,3])
        self.assertFalse(sol.isSymmetric(root))
                           
if __name__ == "__main__":
    unittest.main()