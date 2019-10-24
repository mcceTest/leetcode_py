import unittest

from listNode import ListNode
from X83_RemoveDuplicatesfromSortedList import Solution

class TestSum(unittest.TestCase):

    def test1(self):
        sol = Solution()
        head = ListNode.constructFromList([1,1,2])

        self.assertTrue(sol.deleteDuplicates(head).equalToList([1, 2]))
    
    def test2(self):
        sol = Solution()
        head = ListNode.constructFromList([1,1,2,3,3])

        self.assertTrue(sol.deleteDuplicates(head).equalToList([1, 2, 3]))


if __name__ == "__main__":
    unittest.main()