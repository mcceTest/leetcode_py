import unittest
from X95_UniqueBinarySearchTreesII import Solution
from treeNode import TreeNode

class TestSum(unittest.TestCase):

    def test1(self):
        sol = Solution()
        trees = sol.generateTrees(3)

        treeStrs = map(lambda tree: TreeNode.toList(tree), trees)
        self.assertListEqual(sorted(treeStrs), sorted([[1, None, 2, None, 3],
                                                        [1, None, 3, 2],
                                                        [2, 1, 3],
                                                        [3, 1, None, None, 2],
                                                        [3, 2, None, 1]]))
        
                           
if __name__ == "__main__":
    unittest.main()