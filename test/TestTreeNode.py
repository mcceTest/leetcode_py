from treeNode import TreeNode
import unittest

class TestSum(unittest.TestCase):

    def testConstructFromLevelList1(self):
        root = TreeNode.constructFromLevelList([1, None, 2, 3])

        self.assertIsNotNone(root)
        self.assertEqual(root.val, 1)

        self.assertIsNone(root.left)

        self.assertIsNotNone(root.right)
        self.assertEqual(root.right.val, 2)

        self.assertIsNotNone(root.right.left)
        self.assertEqual(root.right.left.val, 3)

        self.assertIsNone(root.right.right)

if __name__ == "__main__":
    import sys
    unittest.main()