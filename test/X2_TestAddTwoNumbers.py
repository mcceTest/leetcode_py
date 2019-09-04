import unittest
from X2_AddTwoNumbers import Solution

from listNode import ListNode

class TestSum(unittest.TestCase):

    def test1(self):
        sol = Solution()

        l1 = ListNode.constructFromList([2, 4, 3])
        
        l2 = ListNode.constructFromList([5, 6, 4])

        self.assertTrue(sol.addTwoNumbers(l1, l2).equalToList([7, 0, 8]))


    def test2(self):
        sol = Solution()

        l1 = ListNode.constructFromList([2, 4, 9, 1])
        
        l2 = ListNode.constructFromList([5, 6, 4])

        self.assertTrue(sol.addTwoNumbers(l1, l2).equalToList([7, 0, 4, 2]))


    def test3(self):
        sol = Solution()

        l1 = ListNode.constructFromList([2, 4, 9])
        
        l2 = ListNode.constructFromList([5, 6, 4])

        self.assertTrue(sol.addTwoNumbers(l1, l2).equalToList([7, 0, 4, 1]))


    def test4(self):
        sol = Solution()

        l1 = ListNode.constructFromList([2, 4, 9])
        
        l2 = ListNode.constructFromList([0])

        self.assertTrue(sol.addTwoNumbers(l1, l2).equalToList([2, 4, 9]))


if __name__ == "__main__":
    unittest.main()