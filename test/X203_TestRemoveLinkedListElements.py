import unittest
from X203_RemoveLinkedListElements import Solution
from listNode import ListNode

class TestSum(unittest.TestCase):

    def test1(self):
        sol = Solution()
        head = ListNode.constructFromList([1,2,6,3,4,5,6])
        val = 6
        head = sol.removeElements(head, val)
        self.assertTrue(head.equalToList([1,2,3,4,5]))


    def test2(self):
        sol = Solution()
        head = ListNode.constructFromList([6, 1,2,6,3,4,5,6])
        val = 6
        head = sol.removeElements(head, val)
        self.assertTrue(head.equalToList([1,2,3,4,5]))
    

if __name__ == "__main__":
    unittest.main()