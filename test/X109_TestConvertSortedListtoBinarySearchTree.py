import unittest
from X109_ConvertSortedListtoBinarySearchTree import Solution
from listNode import ListNode
from treeNode import TreeNode
class TestSum(unittest.TestCase):

    def test1(self):
        sol = Solution()
        nums = [-10,-3,0,5,9]
        head = ListNode.constructFromList(nums)
        root = sol.sortedListToBST(head)

        # not the only solution
        self.assertTrue(TreeNode.isSameTree(root, TreeNode.constructFromLevelList([0, -10, 5, None, -3, None, 9])))

if __name__ == "__main__":
    unittest.main()