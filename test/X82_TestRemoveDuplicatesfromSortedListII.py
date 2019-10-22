import unittest

from listNode import ListNode
from X82_RemoveDuplicatesfromSortedListII import Solution

class TestSum(unittest.TestCase):

    def test1(self):
        sol = Solution()
        head = ListNode.constructFromList([1,2,3,3,4,4,5])

        self.assertTrue(sol.deleteDuplicates(head).equalToList([1, 2, 5]))
    
    def test2(self):
        sol = Solution()
        head = ListNode.constructFromList([1,1,1,2,3])

        self.assertTrue(sol.deleteDuplicates(head).equalToList([2, 3]))

    def test3(self):
        sol = Solution()
        head = ListNode.constructFromList([1,1,1,2,2])

        self.assertIsNone(sol.deleteDuplicates(head))


if __name__ == "__main__":
    unittest.main()