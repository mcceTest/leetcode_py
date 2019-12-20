import unittest
from X103_BinaryTreeZigzagLevelOrderTraversal import Solution
from treeNode import TreeNode
class TestSum(unittest.TestCase):

    def test1(self):
        sol = Solution()
        root = TreeNode.constructFromLevelList([3,9,20,None,None,15,7])
        self.assertListEqual(sol.zigzagLevelOrder(root), [
                                                    [3],
                                                    [20,9],
                                                    [15,7]
                                                    ])

    def test2(self):
        sol = Solution()
        self.assertListEqual(sol.zigzagLevelOrder(None), [
                                                    
                                                    ])
                           
if __name__ == "__main__":
    unittest.main()