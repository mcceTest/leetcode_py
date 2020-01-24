import unittest
from X138_CopyListwithRandomPointer import Solution, Node

class TestSum(unittest.TestCase):

    def test1(self):
        sol = Solution()
        # head = [[7,null],[13,0],[11,4],[10,2],[1,0]]
        n1 = Node(7)
        n2 = Node(13)
        n3 = Node(11)
        n4 = Node(10)
        n5 = Node(1)

        n1.next = n2
        n2.next = n3
        n3.next = n4
        n4.next = n5

        n2.random = n1
        n3.random = n5
        n4.random = n3
        n5.random = n1

        n = sol.copyRandomList(n1)

        self.assertEqual(n.val, 7)
        self.assertEqual(n.next.val, 13)
        self.assertEqual(n.next.random.val, 7)


if __name__ == "__main__":
    unittest.main()