import unittest
from X96_UniqueBinarySearchTrees import Solution
from treeNode import TreeNode

class TestSum(unittest.TestCase):

    def test1(self):
        sol = Solution()
        self.assertEqual(sol.numTrees(3), 5)
        
                           
if __name__ == "__main__":
    unittest.main()