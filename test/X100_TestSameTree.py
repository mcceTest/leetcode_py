import unittest
from X100_SameTree import Solution
from treeNode import TreeNode
class TestSum(unittest.TestCase):

    def test1(self):
        sol = Solution()
        p = TreeNode.constructFromLevelList([1,2,3])
        q = TreeNode.constructFromLevelList([1,2,3])
        self.assertTrue(sol.isSameTree(p, q))
        
    def test2(self):
        sol = Solution()
        p = TreeNode.constructFromLevelList([1,2])
        q = TreeNode.constructFromLevelList([1,None, 2])
        self.assertFalse(sol.isSameTree(p, q))

    def test3(self):
        sol = Solution()
        p = TreeNode.constructFromLevelList([1,2,1])
        q = TreeNode.constructFromLevelList([1,1,2])
        self.assertFalse(sol.isSameTree(p, q))
                           
if __name__ == "__main__":
    unittest.main()