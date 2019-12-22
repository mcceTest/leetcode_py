import unittest
from X111_MinimumDepthofBinaryTree import Solution
from listNode import ListNode
from treeNode import TreeNode
class TestSum(unittest.TestCase):

    def test1(self):
        sol = Solution()
        root = TreeNode.constructFromLevelList([3,9,20,None,None,15,7])
        self.assertEqual(sol.minDepth(root), 2)


if __name__ == "__main__":
    unittest.main()