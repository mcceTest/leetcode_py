import unittest
from X110_BalancedBinaryTree import Solution
from listNode import ListNode
from treeNode import TreeNode
class TestSum(unittest.TestCase):

    def test1(self):
        sol = Solution()
        root = TreeNode.constructFromLevelList([3,9,20,None,None,15,7])
        self.assertTrue(sol.isBalanced(root))


    def test2(self):
        sol = Solution()
        root = TreeNode.constructFromLevelList([1,2,2,3,3,None,None,4,4])
        self.assertFalse(sol.isBalanced(root))



if __name__ == "__main__":
    unittest.main()