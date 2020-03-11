import unittest
from X206_ReverseLinkedList import Solution
from listNode import ListNode


class TestSum(unittest.TestCase):

    def test1(self):
        sol = Solution()
        head = ListNode.constructFromList([1,2,3,4,5])
        self.assertTrue(sol.reverseList(head).equalToList([5,4,3,2,1]))


    def test2(self):
        sol = Solution()
        head = ListNode.constructFromList([1])
        self.assertTrue(sol.reverseList(head).equalToList([1]))
    

if __name__ == "__main__":
    unittest.main()