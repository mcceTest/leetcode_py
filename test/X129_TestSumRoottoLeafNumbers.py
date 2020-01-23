import unittest
from X129_SumRoottoLeafNumbers import Solution
from treeNode import TreeNode


class TestSum(unittest.TestCase):

    def test1(self):
        sol = Solution()
        root = TreeNode.constructFromLevelList([1,2,3])
        self.assertEqual(sol.sumNumbers(root), 25)

    def test2(self):
        sol = Solution()
        root = TreeNode.constructFromLevelList([4,9,0,5,1])
        self.assertEqual(sol.sumNumbers(root), 1026)

    def test3(self):
        sol = Solution()
        root = TreeNode.constructFromLevelList([4, 1])
        self.assertEqual(sol.sumNumbers(root), 41)

    def test4(self):
        sol = Solution()
        root = TreeNode.constructFromLevelList([4, None, 1])
        self.assertEqual(sol.sumNumbers(root), 41)


if __name__ == "__main__":
    unittest.main()