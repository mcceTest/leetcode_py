import unittest
from X147_InsertionSortList import Solution
from listNode import ListNode


class TestSum(unittest.TestCase):

    def test1(self):
        sol = Solution()
        head = ListNode.constructFromList([4,2,1,3])
        head = sol.insertionSortList(head)
        self.assertTrue(head.equalToList([1,2,3,4]))


    def test2(self):
        sol = Solution()
        head = ListNode.constructFromList([-1,5,3,4,0])
        head = sol.insertionSortList(head)
        self.assertTrue(head.equalToList([-1,0,3,4,5]))

    def test3(self):
        sol = Solution()
        head = ListNode.constructFromList([-1])
        head = sol.insertionSortList(head)
        self.assertTrue(head.equalToList([-1]))

    def test4(self):
        sol = Solution()
        head = ListNode.constructFromList([])
        head = sol.insertionSortList(head)
        self.assertIsNone(head)

if __name__ == "__main__":
    unittest.main()