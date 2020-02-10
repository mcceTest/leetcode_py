import unittest
from X173_BinarySearchTreeIterator import BSTIterator
from treeNode import TreeNode


class TestSum(unittest.TestCase):

    def test1(self):
        root = TreeNode.constructFromLevelList([7,3,15,None, None, 9, 20])
        it = BSTIterator(root)
        self.assertEqual(it.next(),3) 
        self.assertEqual(it.next(),7) 
        self.assertTrue(it.hasNext())
        self.assertEqual(it.next(),9) 
        self.assertTrue(it.hasNext())
        self.assertEqual(it.next(),15) 
        self.assertTrue(it.hasNext())
        self.assertEqual(it.next(),20) 
        self.assertFalse(it.hasNext())


if __name__ == "__main__":
    unittest.main()