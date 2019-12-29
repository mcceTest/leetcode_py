import unittest
from X116_PopulatingNextRightPointersinEachNode import Solution, Node
class TestSum(unittest.TestCase):

    def test1(self):
        sol = Solution()
        root = Node(1)
        root.left = Node(2)
        root.right = Node(3)

        root.left.left = Node(4)
        root.left.right = Node(5)

        root.right.left = Node(6)
        root.right.right = Node(7)

        root = sol.connect(root)

        self.assertIsNone(root.next)
        self.assertEqual(root.left.next.val, 3)
        self.assertIsNone(root.right.next)

        self.assertEqual(root.left.left.next.val, 5)
        self.assertEqual(root.left.right.next.val, 6)
        self.assertEqual(root.right.left.next.val, 7)
        self.assertIsNone(root.right.right.next)


if __name__ == "__main__":
    unittest.main()