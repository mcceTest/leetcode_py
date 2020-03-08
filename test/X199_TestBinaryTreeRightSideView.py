import unittest
from X199_BinaryTreeRightSideView import Solution
from treeNode import TreeNode

class TestSum(unittest.TestCase):

    def test1(self):
        sol = Solution()
        root = TreeNode.constructFromLevelList([1,2,3,None,5,None,4])
        self.assertListEqual(sol.rightSideView(root), [1,3,4])


    def test2(self):
        sol = Solution()
        root = TreeNode.constructFromLevelList([1,2,None])
        self.assertListEqual(sol.rightSideView(root), [1,2])

    

if __name__ == "__main__":
    unittest.main()