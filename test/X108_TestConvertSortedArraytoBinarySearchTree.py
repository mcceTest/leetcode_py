import unittest
from X108_ConvertSortedArraytoBinarySearchTree import Solution
from treeNode import TreeNode
class TestSum(unittest.TestCase):

    def test1(self):
        sol = Solution()
        nums = [-10,-3,0,5,9]
        root = sol.sortedArrayToBST(nums)

        # this is not the only answer
        self.assertTrue(TreeNode.isSameTree(root, TreeNode.constructFromLevelList([0, -10, 5, None, -3, None, 9])))


if __name__ == "__main__":
    unittest.main()