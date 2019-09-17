import unittest

from X21_MergeTwoSortedLists import Solution
from listNode import ListNode

class TestSum(unittest.TestCase):

    def test1(self):
        sol = Solution()

        sol = Solution()

        l1 = ListNode.constructFromList([1, 2, 4])
        l2 = ListNode.constructFromList([1, 3, 4])

        head = sol.mergeTwoLists(l1, l2)

        self.assertTrue(head.equalToList([1, 1, 2, 3, 4, 4]))


    def test2(self):
        sol = Solution()

        sol = Solution()

        l1 = ListNode.constructFromList([])
        l2 = ListNode.constructFromList([1, 3, 4])

        head = sol.mergeTwoLists(l1, l2)

        self.assertTrue(head.equalToList([1, 3, 4]))
        
       
if __name__ == "__main__":
    unittest.main()